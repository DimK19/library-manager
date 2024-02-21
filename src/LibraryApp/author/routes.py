from flask import render_template, redirect, url_for, request, flash, abort
from LibraryApp import app, DB, utilities
from LibraryApp.author import author
import sqlite3

### Get indexed list of authors ###
@author.route('/author', methods = ['GET'])
def get_authors():
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

### Update author ###
@author.route('/author/update', methods = ['GET', 'POST'])
def update_author():
    if(request.method == 'GET'):
        connection = sqlite3.connect(DB)
        authors = []
        with connection:
            cur = connection.cursor()
            query = 'SELECT * FROM `author`;'
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            authors = sorted([dict(zip(column_names, entry)) for entry in cur.fetchall()], key = lambda x: x['last_name'])
        return render_template('update_author.html', authors = authors)
    else:
        data = request.form
        first_name = data.get('authorFirstName')
        if(first_name == ''):
            first_name = 'NULL'
        else:
            first_name = utilities.foo(first_name)
        last_name = data.get('authorLastName')
        last_name = utilities.foo(last_name)
        author_id = data.get('authorId')
        query = f'''UPDATE `author`
                  SET first_name = "{first_name}", last_name = "{last_name}"
                  WHERE id = {author_id};'''
        connection = sqlite3.connect(DB)
        with connection:
            cur = connection.cursor()
            cur.execute(query)
        return render_template('update_index.html')
