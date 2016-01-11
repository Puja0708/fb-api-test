# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
DATABASE = ''
DEBUG = True
SECRET_KEY = ''
USERNAME = ''
PASSWORD = ''