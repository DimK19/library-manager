from flask import render_template, redirect, url_for, request, flash, abort
from LibraryApp import DB, utilities
from LibraryApp.collection import collection
import sqlite3

### Get indexed list of collections ###
@collection.route('/collection', methods = ['GET'])
def collection():
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
