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
def index():
    return render_template('index.html')

### Index page for updates ###
@app.route('/update', methods = ['GET'])
def update_index():
    return render_template('update_index.html')
