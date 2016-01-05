from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth
from flask_sqlalchemy import SQLAlchemy
import json
import requests


ACCESS_TOKEN = 'CAACEdEose0cBAMi8kuWP7i7QnhqERrwohfKOaTNLl2sL5HqoJBhsLog4zvm8oXk6ZBfdch6vDMA9MZArYMDfnmpUva4EmAYkXQJDZCOvvZCN8VYl8pDxZBNipuXghXyiCmZAM0uv6ggKGuDe681N5smo7ncYzrWufByBFjs1H30nYsePIElXtO9rrXweLOpzkZD'
DEBUG = True
app = Flask(__name__)
app.debug = DEBUG
oauth = OAuth()

base_url = 'https://graph.facebook.com/v2.2/'
likes = '116151972998_10153804678607999/likes?access_token=' #replace the post_id
post = '116151972998_10153804678607999?access_token='

#we are using the facebook graph API version 2.2, instead of the latest one(2.5)
def get_data_from_page_id():
	url = 'https://graph.facebook.com/v2.2/116151972998/posts?access_token=CAACEdEose0cBAJrlYiLOjGAqyogCjdUer0vBh8LMECHCR0FCaxfZBTo1FOB7omxtXu8mvS1woFRf8MitoKZCdfAJUtr4tuVIp9gyJIcuK43m1nbZAJBifFo2A1PZBy68RRBIGpZCG5f4AWLsOxOmD7IgmNWmW6bd3eaePDqysWYJkkM3RvmNAXi4jTYTpATXks2T1ebZCL8gZDZD'
	response = requests.get(url)
	json_data = json.loads(response.text)
	number_of_posts = len(json_data["data"])
	# print json_data["data"][0]["id"]
	# print number_of_posts
	for i in xrange(number_of_posts):
		id = json_data["data"][i]["id"]
		print i, id
	# print number_of_posts_on_the_page
	#generate access token via oauth, once done
	

def get_data_from_page_id_posts():
	return "hello"

def get_data_from_post_id():
	# return "hello"
	url = 'https://graph.facebook.com/v2.2/116151972998/posts?access_token=CAACEdEose0cBAMi8kuWP7i7QnhqERrwohfKOaTNLl2sL5HqoJBhsLog4zvm8oXk6ZBfdch6vDMA9MZArYMDfnmpUva4EmAYkXQJDZCOvvZCN8VYl8pDxZBNipuXghXyiCmZAM0uv6ggKGuDe681N5smo7ncYzrWufByBFjs1H30nYsePIElXtO9rrXweLOpzkZD'
	response = requests.get(url)
	json_data = json.loads(response.text)
	number_of_posts = len(json_data["data"])



def get_number_of_likes_on_post():
	url = base_url + likes + ACCESS_TOKEN
	#print url
	response = requests.get(url)
	json_data = json.loads(response.text)
	length = len(json_data)
	data = json_data["data"]
	number_of_likes = len(data)
	# return json_data
	return number_of_likes

def get_comment_count_on_post():
	url = 'https://graph.facebook.com/v2.2/116151972998_10153804678607999/comments?access_token=CAACEdEose0cBAMi8kuWP7i7QnhqERrwohfKOaTNLl2sL5HqoJBhsLog4zvm8oXk6ZBfdch6vDMA9MZArYMDfnmpUva4EmAYkXQJDZCOvvZCN8VYl8pDxZBNipuXghXyiCmZAM0uv6ggKGuDe681N5smo7ncYzrWufByBFjs1H30nYsePIElXtO9rrXweLOpzkZD'
	response = requests.get(url)
	json_data = json.loads(response.text)
	number_of_comments = len(json_data["data"])
	print number_of_comments


def get_author_name():
	url = base_url + post + ACCESS_TOKEN
	response = requests.get(url)
	json_data = json.loads(response.text)
	author_name = json_data["admin_creator"]["name"]
	print author_name
	# print url


# @facebook.tokengetter
# def get_facebook_oauth_token():
#     return session.get('oauth_token')

# a = get_number_of_likes_on_post()
# print a

# get_author_name()
# get_comment_count_on_post()
# print(x, end=" ")

# if __name__ == '__main__':
#     app.run()
# get_data_from_post_id()
get_data_from_page_id()