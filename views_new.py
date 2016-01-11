from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth
from flask_sqlalchemy import SQLAlchemy
import json
import requests
import sqlite3


ACCESS_TOKEN = 'CAACEdEose0cBAKTE1SgAIrAKkwi6WLMtg4QN28ZCkNDebFCZCK0c70MwEjnKIltZCJtz5PSJcZAzZC6zZAUx3p1sEkXzZCTkPTs92gb7bZCbIIgOThQwrWiTFkt1VcoTwCjibZBM6X89iNdjGBRI2aKw437kKkosVdBV44bVxJUUScuFdPCBcT6wWtqPZAhTuag1pmbZArS95I2KQwZATK1C77k4'
DEBUG = True
app = Flask(__name__)
app.debug = DEBUG
oauth = OAuth()
data = {}
data1 = []
# json_array = []


def get_data():
	url = 'http://127.0.0.1:5000/fb-api'
	response = requests.get(url)
	json_data = json.loads(response.text)
	return json_data

a = get_data()
print a