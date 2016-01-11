# from flask import Flask, redirect, url_for, session, request
# from flask_oauth import OAuth
# from views import get_number_of_likes_on_post, get_comment_count_on_post, get_author_name
# from flask import render_template
from flask import Flask, Markup
from flask import render_template
# from views import get_number_of_likes_on_post, get_author_name, get_data_from_page_id
from views_new import get_data

app = Flask(__name__)
data = ''
@app.route('/')
def hello_world():
	data = get_data()
	return render_template('index.html', data=data)
	# return render_template('index.html', page_name='SportsKeeda', data=data)
	# for i in xrange(0,25):
		# id = get_data_from_page_id()
		# id = str(id)
		# post_id = '116151972998_10153809342577999'
		# for i in xrange(0,25):
			# post_id = get_data_from_page_id(i)
			# likes = get_number_of_likes_on_post(post_id) + i
			# post_title = get_post_title(post_id)
			# author = get_author_name(post_id)
			# post_title, author = get_author_name(post_id)
			# print post_id, likes, post_title, author
			# return render_template('index.html', page_name='SportsKeeda',likes=likes, post_id=post_id, post_title=post_title, author=author)
		# return render_template('index.html', page_name='SportsKeeda',likes=likes, post_id=post_id, post_title=post_title, author=author)
	# return 'Hello World!'

# @app.route('/test')
# def test_json_data():
# 	return render_template('test_json.html')

# @app.route('/foo')
# def next():
# 	data1 = get_data()
# 	# print data
# 	return render_template('index.html', data1=data1)

if __name__ == '__main__':
	app.run(port=1234, debug=True)
# hello_world()