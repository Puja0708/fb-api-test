from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth
from views import get_number_of_likes_on_post, get_comment_count_on_post, get_author_name

app = Flask(__name__)

@app.route('/')
# @templated('index.html')
def index():
	# return render_template('index.html')
	return "Hello"

app.run()

a = get_author_name()
print a