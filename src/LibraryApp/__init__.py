from flask import Flask
import sqlite3
from LibraryApp.book import book
from LibraryApp.collection import collection
from LibraryApp.author import author
from LibraryApp.publisher import publisher

DB = 'library_database.db'
app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'

app.app_context().push()

from LibraryApp import routes, utilities
from LibraryApp.book import routes
from LibraryApp.collection import routes
from LibraryApp.author import routes
from LibraryApp.publisher import routes
app.register_blueprint(book)
app.register_blueprint(collection)
app.register_blueprint(author)
app.register_blueprint(publisher)
