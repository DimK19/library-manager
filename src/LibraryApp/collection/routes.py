from flask import render_template, redirect, url_for, request, flash, abort
from LibraryApp import DB, utilities
from LibraryApp.collection import collection
import sqlite3

### Get indexed list of collections ###
@collection.route('/collection', methods = ['GET'])
def get_collections():
    connection = sqlite3.connect(DB)
    books = []
    sorted_by_type = {}
    with connection:
        cur = connection.cursor()
        query = '''SELECT c.*, ct.category FROM `collection` c
                   INNER JOIN `collection_type` ct
                   ON c.collection_type_id = ct.id;'''
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

### Get indexed list of collections ###
@collection.route('/collection/update', methods = ['GET', 'POST'])
def update_collection():
    if(request.method == 'GET'):
        connection = sqlite3.connect(DB)
        collections = []
        with connection:
            cur = connection.cursor()
            query = 'SELECT * FROM `collection`;'
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            collections = sorted(
                [dict(zip(column_names, entry)) for entry in cur.fetchall()],
                key = lambda x: x['title'])
            query = 'SELECT * FROM `collection_type`;'
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            collection_types = sorted(
                [dict(zip(column_names, entry)) for entry in cur.fetchall()],
                key = lambda x: x['category'])
        return render_template('update_collection.html',
                               collections = collections,
                               collection_types = collection_types)
    else:
        print('in controller')
        data = request.form
        print(data)
        collection_name = data.get('collectionName')
        collection_name = utilities.foo(collection_name)
        collection_id = data.get('collectionId')
        collection_type_id = data.get('collectionType')
        query = f'''UPDATE `collection`
                  SET title = "{collection_name}", collection_type_id = {collection_type_id}
                  WHERE id = {collection_id};'''
        try:
            connection = sqlite3.connect(DB)
            with connection:
                cur = connection.cursor()
                cur.execute(query)
            flash('Επιτυχής διόρθωση συλλογής.', 'primary')
        except Exception as e:
            flash(e, 'danger')
        return redirect(url_for('update_index'))
