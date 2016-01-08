import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing

# configuration
DATABASE = '/home/puja/Documents/fb-api-test/flaskr.db'
DEBUG = True
SECRET_KEY = ' '
USERNAME = ' '
PASSWORD = ' '

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
    print "db connected"

if __name__ == '__main__':
    app.run()
