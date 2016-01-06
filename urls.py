# from flask import Flask, redirect, url_for, session, request
# from flask_oauth import OAuth
# from views import get_number_of_likes_on_post, get_comment_count_on_post, get_author_name
# from flask import render_template
from flask import Flask, Markup
from flask import render_template
from views import get_number_of_likes_on_post, get_comment_count_on_post, get_author_name, get_data_from_page_id, get_post_title

app = Flask(__name__)

# @app.route('/')
def hello_world():
	for i in xrange(0,25):
		# id = get_data_from_page_id()
		# id = str(id)
		# post_id = '116151972998_10153809342577999'
		for i in xrange(0,25):
			post_id = get_data_from_page_id(i)
			likes = get_number_of_likes_on_post(post_id) + i
			post_title = get_post_title(post_id)
			author = get_author_name(post_id)
			print post_id, likes, post_title, author
			return render_template('index.html', page_name='SportsKeeda',likes=likes, post_id=post_id, post_title=post_title, author=author)
		# return render_template('index.html', page_name='SportsKeeda',likes=likes, post_id=post_id, post_title=post_title, author=author)
	# return 'Hello World!'

# @app.route('/test')
# def test_json_data():
# 	return render_template('test_json.html')

# if __name__ == '__main__':
# 	app.run(port=1234, debug=True)
hello_world()