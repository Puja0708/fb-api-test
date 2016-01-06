from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth
from flask_sqlalchemy import SQLAlchemy
import json
import requests


ACCESS_TOKEN = 'CAACEdEose0cBALItxv1Kau2TSzGJEsIJCdl3eQZBlZCkLc2ZCQaVtIZBNLMNlEZCiOt997FKvTZAmH7KZBmnMsiMfSMy6tSV132xpxYN466QQhRFjhJIg1IxtWjkLfNdIoHQv9VIUNGPLwINm2EUSq0cRZCJX7aO01oxocga4o4aGWCn8BB5o9lm9qbcKENlrzLtBJMdIg8TMQZDZD'
DEBUG = True
app = Flask(__name__)
app.debug = DEBUG
oauth = OAuth()
# json_array = []

base_url = 'https://graph.facebook.com/v2.2/'
likes = '116151972998_10153804678607999/likes?access_token=' #replace the post_id
post = '116151972998_10153804678607999?access_token='

#we are using the facebook graph API version 2.2, instead of the latest one(2.5)
def get_data_from_page_id(i):
	url = 'https://graph.facebook.com/v2.2/116151972998/posts?access_token=CAACEdEose0cBALItxv1Kau2TSzGJEsIJCdl3eQZBlZCkLc2ZCQaVtIZBNLMNlEZCiOt997FKvTZAmH7KZBmnMsiMfSMy6tSV132xpxYN466QQhRFjhJIg1IxtWjkLfNdIoHQv9VIUNGPLwINm2EUSq0cRZCJX7aO01oxocga4o4aGWCn8BB5o9lm9qbcKENlrzLtBJMdIg8TMQZDZD'
	response = requests.get(url)
	json_data = json.loads(response.text)
	data1 = json_data["data"]
	# post_id_to_be_returned = data1[i]["id"]
	# return post_id_to_be_returned
	post_id_to_be_returned = data1[i]["id"]
	title = data1[i]["name"]
	# print i, title, post_id_to_be_returned
	return post_id_to_be_returned
	
	# number_of_posts = len(json_data["data"])
	# print 'blah'
	# for i in xrange(number_of_posts):
	# 	id = json_data["data"][i]["id"]
	# 	likes_on_post = get_number_of_likes_on_post(id)
		
	# 	return likes_on_post
		
	#generate access token via oauth, once done
	

def get_data_from_page_id_posts():
	return "hello"

def get_data_from_post_id():
	# return "hello"
	url = 'https://graph.facebook.com/v2.2/116151972998/posts?access_token=CAACEdEose0cBALItxv1Kau2TSzGJEsIJCdl3eQZBlZCkLc2ZCQaVtIZBNLMNlEZCiOt997FKvTZAmH7KZBmnMsiMfSMy6tSV132xpxYN466QQhRFjhJIg1IxtWjkLfNdIoHQv9VIUNGPLwINm2EUSq0cRZCJX7aO01oxocga4o4aGWCn8BB5o9lm9qbcKENlrzLtBJMdIg8TMQZDZD'
	response = requests.get(url)
	json_data = json.loads(response.text)
	number_of_posts = len(json_data["data"])



def get_number_of_likes_on_post(id):
	# url = base_url + likes + ACCESS_TOKEN
	url = base_url + id + '/likes?access_token=' + ACCESS_TOKEN
	
	response = requests.get(url)
	json_data = json.loads(response.text)
	length = len(json_data)
	data1 = json_data["data"]
	number_of_likes = len(data1)
	return number_of_likes
	# return number_of_likes

def get_comment_count_on_post():
	url = 'https://graph.facebook.com/v2.2/116151972998_10153804678607999/comments?access_token=CAACEdEose0cBALItxv1Kau2TSzGJEsIJCdl3eQZBlZCkLc2ZCQaVtIZBNLMNlEZCiOt997FKvTZAmH7KZBmnMsiMfSMy6tSV132xpxYN466QQhRFjhJIg1IxtWjkLfNdIoHQv9VIUNGPLwINm2EUSq0cRZCJX7aO01oxocga4o4aGWCn8BB5o9lm9qbcKENlrzLtBJMdIg8TMQZDZD'
	response = requests.get(url)
	json_data = json.loads(response.text)
	number_of_comments = len(json_data["data"])
	

def get_author_name(id):
	# url = base_url + post + ACCESS_TOKEN
	url = 'https://graph.facebook.com/v2.2/' + id +'?access_token=CAACEdEose0cBALItxv1Kau2TSzGJEsIJCdl3eQZBlZCkLc2ZCQaVtIZBNLMNlEZCiOt997FKvTZAmH7KZBmnMsiMfSMy6tSV132xpxYN466QQhRFjhJIg1IxtWjkLfNdIoHQv9VIUNGPLwINm2EUSq0cRZCJX7aO01oxocga4o4aGWCn8BB5o9lm9qbcKENlrzLtBJMdIg8TMQZDZD'
	response = requests.get(url)
	json_data = json.loads(response.text)
	author_name = json_data["admin_creator"]["name"]
	return author_name

def get_post_title(id):
	url = 'https://graph.facebook.com/v2.2/' + id +'?access_token=CAACEdEose0cBALItxv1Kau2TSzGJEsIJCdl3eQZBlZCkLc2ZCQaVtIZBNLMNlEZCiOt997FKvTZAmH7KZBmnMsiMfSMy6tSV132xpxYN466QQhRFjhJIg1IxtWjkLfNdIoHQv9VIUNGPLwINm2EUSq0cRZCJX7aO01oxocga4o4aGWCn8BB5o9lm9qbcKENlrzLtBJMdIg8TMQZDZD'
	# print url
	response = requests.get(url)
	json_data = json.loads(response.text)
	title = json_data["name"]
	return title	
	# print url


# @facebook.tokengetter
# def get_facebook_oauth_token():
#     return session.get('oauth_token')

# a = get_number_of_likes_on_post()


# get_author_name()
# get_comment_count_on_post()

# if __name__ == '__main__':
#     app.run()
# get_data_from_post_id()
# get_data_from_page_id()
# get_number_of_likes_on_post('116151972998_10153809342577999')
# get_post_title('116151972998_10153809426852999')
def get_json_all():
	data = {}
	data["post_id"]='aaa'
	data['author_name'] = 'bbb'
	print data
	json_data1 = json.loads(json.dumps(data, ensure_ascii=False))
	print json_data1
	print json_data1["post_id"]

	
get_json_all()