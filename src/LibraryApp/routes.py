from flask import render_template, redirect, url_for, request, flash, abort
from LibraryApp import app, DB, utilities
import sqlite3

### ERROR HANDLERS START ###
@app.errorhandler(404)
def page_not_found(e):
    ## note that the 404 status is set explicitly
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500
### ERROR HANDLERS END ###

### Opening page ###
@app.route('/')
def root():
    return render_template('index.html')

### Record book ###
@app.route('/book/record', methods = ['GET', 'POST'])
def new_book():
    if(request.method == 'POST'):
        form = request.get_json()

        ## TITLE
        title = form.get('title')
        title = utilities.foo(title)

        ## AUTHOR OR AUTHORS
        authors = form.get('authors')
        author_ids = []
        for x in authors:
            if(not (x.get('lastName') is None)):
                first_name = x.get('firstName')
                if(first_name is None):
                    first_name = 'NULL'
                else:
                    first_name = utilities.foo(first_name)
                last_name = x.get('lastName')
                last_name = utilities.foo(last_name)
                query = f'INSERT INTO `author` (first_name, last_name) VALUES ("{first_name}", "{last_name}");'
                connection = sqlite3.connect(DB)
                with connection:
                    cur = connection.cursor()
                    cur.execute(query)
                    author_ids.append(cur.lastrowid)
            else:
                author_ids.append(x.get('id'))

        ## PUBLISHER
        p = form.get('publisher')
        publisher_id = None
        if(not (p.get('id') is None)):
            publisher_id = p.get('id')
        else:
            np = p.get('newPublisherName')
            np = utilities.foo(np)
            query = f'INSERT INTO `publisher` (name) VALUES ("{np}");'
            connection = sqlite3.connect(DB)
            with connection:
                cur = connection.cursor()
                cur.execute(query)
                publisher_id = cur.lastrowid

        ## EDITION
        edition = form.get('edition')
        if(edition is None):
            edition = 'NULL'

        ## LOCATION
        location_id = form.get('location')

        ## SET
        s = form.get('set')
        set_id = 'NULL'
        volume = 'NULL'
        if(not (s is None)):
            if(s.get('id') is None):
                sn = s.get('setName')
                sn = utilities.foo(sn)
                st = s.get('setType')
                query = f'INSERT INTO `collection` (collection_type_id, title) VALUES ({st}, "{sn}");'
                connection = sqlite3.connect(DB)
                with connection:
                    cur = connection.cursor()
                    cur.execute(query)
                    set_id = cur.lastrowid
            else:
                set_id = s.get('id')
            if(not (s.get('volume') is None)):
                volume = s.get('volume')

        ## BOOK
        query = f'INSERT INTO `book` (title, volume, publisher_id, location_id, collection_id, edition) VALUES ("{title}", {volume}, {publisher_id}, {location_id}, {set_id}, {edition});'
        connection = sqlite3.connect(DB)
        with connection:
            cur = connection.cursor()
            cur.execute(query)
            book_id = cur.lastrowid

        ## BOOK_AUTHOR
        try:
            for aid in author_ids:
                query = f'INSERT INTO `book_author` (book_id, author_id) VALUES ({book_id}, {aid});'
                connection = sqlite3.connect(DB)
                with connection:
                    cur = connection.cursor()
                    cur.execute(query)
        except Exception as e:
            print(e)

        return '200'
    else:
        authors = []
        publishers = []
        collections = []
        collection_types = []
        locations = []
        connection = sqlite3.connect(DB)
        with connection:
            cur = connection.cursor()
            query = f'SELECT * FROM `author`;'
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            authors = sorted([dict(zip(column_names, entry)) for entry in cur.fetchall()], key = lambda x: x['last_name'])

            query = f'SELECT * FROM `publisher`;'
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            publishers = sorted([dict(zip(column_names, entry)) for entry in cur.fetchall()], key = lambda x: x['name'])

            query = f'SELECT * FROM `collection`;'
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            collections = sorted([dict(zip(column_names, entry)) for entry in cur.fetchall()], key = lambda x: x['title'])

            query = f'SELECT * FROM `location`;'
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            locations = sorted([dict(zip(column_names, entry)) for entry in cur.fetchall()], key = lambda x: x['place'])

            query = f'SELECT * FROM `collection_type`;'
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            collection_types = sorted([dict(zip(column_names, entry)) for entry in cur.fetchall()], key = lambda x: x['category'])

        return render_template('form_page_new_book.html',
            authors = authors,
            publishers = publishers,
            collections = collections,
            locations = locations,
            collection_types = collection_types
        )

@app.route('/book/all', methods = ['GET'])
def get_books():
    connection = sqlite3.connect(DB)
    books = []
    with connection:
        cur = connection.cursor()
        query = '''SELECT b.id, b.title, p.name, l.place FROM `book` b
                   INNER JOIN `publisher` p ON b.publisher_id = p.id
                   INNER JOIN `location` l ON b.location_id = l.id;'''
        cur.execute(query)
        column_names = [i[0] for i in cur.description]
        books = sorted([dict(zip(column_names, entry)) for entry in cur.fetchall()], key = lambda x: x['title'])

        query = 'SELECT id FROM `book`;'
        cur.execute(query)
        column_names = [i[0] for i in cur.description]
        onlybooks = [dict(zip(column_names, entry)) for entry in cur.fetchall()]

        for ob in onlybooks:
            query = f'''SELECT ba.book_id, a.* FROM `author` a
                        INNER JOIN `book_author` ba ON a.id = ba.author_id
                        WHERE ba.book_id = {ob["id"]};'''
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            temp = [dict(zip(column_names, entry)) for entry in cur.fetchall()]

            for b in books:
                for t in temp:
                    if(b['id'] == t['book_id']):
                        if(not ('authors' in b)):
                            b['authors'] = []
                        b['authors'].append({'first_name': t['first_name'], 'last_name': t['last_name']})
        for b in books:
            b['authors'] = ', '.join([f'{(x["first_name"] + " ") if x["first_name"] != "NULL" else ""}{x["last_name"]}' for x in b['authors']])

    return render_template('books.html', books = books)

@app.route('/books', methods = ['GET'])
def get_books_with_criterion():
    req_parameters = dict(request.args)
    if('collection_id' in req_parameters):
        connection = sqlite3.connect(DB)
        books = []
        with connection:
            cur = connection.cursor()
            query = f'''SELECT b.id, b.title, p.name, l.place FROM `book` b
                        INNER JOIN `publisher` p ON b.publisher_id = p.id
                        INNER JOIN `location` l ON b.location_id = l.id
                        WHERE b.collection_id = {req_parameters["collection_id"]};'''
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            books = sorted([dict(zip(column_names, entry)) for entry in cur.fetchall()], key = lambda x: x['title'])

            query = 'SELECT id FROM `book`;'
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            onlybooks = [dict(zip(column_names, entry)) for entry in cur.fetchall()]

            for ob in onlybooks:
                query = f'''SELECT ba.book_id, a.* FROM `author` a
                            INNER JOIN `book_author` ba ON a.id = ba.author_id
                            WHERE ba.book_id = {ob["id"]};'''
                cur.execute(query)
                column_names = [i[0] for i in cur.description]
                temp = [dict(zip(column_names, entry)) for entry in cur.fetchall()]

                for b in books:
                    for t in temp:
                        if(b['id'] == t['book_id']):
                            if(not ('authors' in b)):
                                b['authors'] = []
                            b['authors'].append({'first_name': t['first_name'], 'last_name': t['last_name']})
            for b in books:
                b['authors'] = ', '.join([f'{(x["first_name"] + " ") if x["first_name"] != "NULL" else ""}{x["last_name"]}' for x in b['authors']])

        return render_template('books.html', books = books)

    elif('author_id' in req_parameters):
        connection = sqlite3.connect(DB)
        books = []
        with connection:
            cur = connection.cursor()
            query = f'''SELECT b.id, b.title, p.name, l.place FROM `book` b
                        INNER JOIN `publisher` p ON b.publisher_id = p.id
                        INNER JOIN `location` l ON b.location_id = l.id
                        INNER JOIN `book_author` ba ON b.id = ba.book_id
                        INNER JOIN `author` a ON a.id = ba.author_id
                        WHERE a.id = {req_parameters["author_id"]};'''
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            books = sorted([dict(zip(column_names, entry)) for entry in cur.fetchall()], key = lambda x: x['title'])

            query = 'SELECT id FROM `book`;'
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            onlybooks = [dict(zip(column_names, entry)) for entry in cur.fetchall()]

            for ob in onlybooks:
                query = f'''SELECT ba.book_id, a.* FROM `author` a
                            INNER JOIN `book_author` ba ON a.id = ba.author_id
                            WHERE ba.book_id = {ob["id"]};'''
                cur.execute(query)
                column_names = [i[0] for i in cur.description]
                temp = [dict(zip(column_names, entry)) for entry in cur.fetchall()]

                for b in books:
                    for t in temp:
                        if(b['id'] == t['book_id']):
                            if(not ('authors' in b)):
                                b['authors'] = []
                            b['authors'].append({'first_name': t['first_name'], 'last_name': t['last_name']})
            for b in books:
                b['authors'] = ', '.join([f'{(x["first_name"] + " ") if x["first_name"] != "NULL" else ""}{x["last_name"]}' for x in b['authors']])

        return render_template('books.html', books = books)

    else:
        return render_template('errors/404.html'), 404

@app.route('/book/search', methods = ['GET', 'POST'])
def search_book():
    books = []
    if(request.method == 'POST'):
        form = request.form

        title = form.get('searchTitle')
        title = utilities.foo(title)
        connection = sqlite3.connect(DB)
        with connection:
            cur = connection.cursor()
            query = f'SELECT b.id, b.title, p.name, l.place FROM `book` b INNER JOIN `publisher` p ON b.publisher_id = p.id INNER JOIN `location` l ON b.location_id = l.id WHERE b.title LIKE "%{title}%";'
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            books = sorted([dict(zip(column_names, entry)) for entry in cur.fetchall()], key = lambda x: x['title'])

            query = 'SELECT id FROM `book`;'
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            onlybooks = [dict(zip(column_names, entry)) for entry in cur.fetchall()]

            for ob in onlybooks:
                query = f'SELECT ba.book_id, a.* FROM `author` a INNER JOIN `book_author` ba ON a.id = ba.author_id WHERE ba.book_id = {ob["id"]};'
                cur.execute(query)
                column_names = [i[0] for i in cur.description]
                temp = [dict(zip(column_names, entry)) for entry in cur.fetchall()]

                for b in books:
                    for t in temp:
                        if(b['id'] == t['book_id']):
                            if(not ('authors' in b)):
                                b['authors'] = []
                            b['authors'].append({'first_name': t['first_name'], 'last_name': t['last_name']})
            for b in books:
                b['authors'] = ', '.join([f'{(x["first_name"] + " ") if x["first_name"] != "NULL" else ""}{x["last_name"]}' for x in b['authors']])

    return render_template('search_book.html', books = books)

@app.route('/collection', methods = ['GET'])
def collection():
    connection = sqlite3.connect(DB)
    books = []
    sorted_by_type = {}
    with connection:
        cur = connection.cursor()
        query = 'SELECT c.*, ct.category FROM `collection` c INNER JOIN `collection_type` ct ON c.collection_type_id = ct.id;'
        cur.execute(query)
        column_names = [i[0] for i in cur.description]
        collections = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        ## SORT BY TYPE
        for c in collections:
            if(c['category'] in sorted_by_type):
                sorted_by_type[c['category']].append(c)
            else:
                sorted_by_type[c['category']] = []
                sorted_by_type[c['category']].append(c)

    return render_template('indexed_list.html', data = sorted_by_type, categories = list(sorted_by_type.keys()), type = 0)

@app.route('/author', methods = ['GET'])
def author():
    connection = sqlite3.connect(DB)
    books = []
    sorted_by_name = {}
    with connection:
        cur = connection.cursor()
        query = 'SELECT * FROM `author`;'
        cur.execute(query)
        column_names = [i[0] for i in cur.description]
        authors = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        ## SORT BY NAME
        for a in authors:
            if(a['last_name'][0] in sorted_by_name):
                sorted_by_name[a['last_name'][0]].append(a)
            else:
                sorted_by_name[a['last_name'][0]] = []
                sorted_by_name[a['last_name'][0]].append(a)


    return render_template('indexed_list.html', data = sorted_by_name, categories = sorted(list(sorted_by_name.keys())), type = 1)
