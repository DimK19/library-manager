from flask import Flask
import sqlite3

DB = 'library_database.db'
app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'

app.app_context().push()

from LibraryApp import routes, utilities
