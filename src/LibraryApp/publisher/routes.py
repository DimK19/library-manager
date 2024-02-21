from flask import render_template, redirect, url_for, request, flash, abort
from LibraryApp import DB, utilities
from LibraryApp.publisher import publisher
import sqlite3

@publisher.route('/publisher/update', methods = ['GET', 'POST'])
def update_publisher():
    if(request.method == 'GET'):
        connection = sqlite3.connect(DB)
        publishers = []
        with connection:
            cur = connection.cursor()
            query = 'SELECT * FROM `publisher`;'
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            publishers = sorted([dict(zip(column_names, entry)) for entry in cur.fetchall()], key = lambda x: x['name'])
        return render_template('update_publisher.html', publishers = publishers)
    else:
        data = request.form
        publisher_name = data.get('publisherName')
        publisher_name = utilities.foo(publisher_name)
        publisher_id = data.get('publisherId')
        query = f'''UPDATE `publisher`
                  SET name = "{publisher_name}"
                  WHERE id = {publisher_id};'''
        connection = sqlite3.connect(DB)
        with connection:
            cur = connection.cursor()
            cur.execute(query)
        return render_template('update_index.html')
