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

base_url = 'https://graph.facebook.com/v2.2/'
likes = '116151972998_10153804678607999/likes?access_token=' #replace the post_id
post = '116151972998_10153804678607999?access_token='

#we are using the facebook graph API version 2.2, instead of the latest one(2.5)
def get_data_from_page_id(i):
	
	url = 'https://graph.facebook.com/v2.2/116151972998/posts?access_token=CAACEdEose0cBAKTE1SgAIrAKkwi6WLMtg4QN28ZCkNDebFCZCK0c70MwEjnKIltZCJtz5PSJcZAzZC6zZAUx3p1sEkXzZCTkPTs92gb7bZCbIIgOThQwrWiTFkt1VcoTwCjibZBM6X89iNdjGBRI2aKw437kKkosVdBV44bVxJUUScuFdPCBcT6wWtqPZAhTuag1pmbZArS95I2KQwZATK1C77k4'
	# response = requests.get(url)
	json_data = connect_url(url)
	# connect_url(url)
	data1 = json_data["data"]
	post_id_to_be_returned = data1[i]["id"]
		# return post_id_to_be_returned
		# post_id_to_be_returned = data1[i]["id"]
	# title = data1[i]["name"]
	if i>25:
		if 'next' in json_data['paging']:
			url = json_data["paging"]["next"]
			post_id_to_be_returned = url
	# print i, title, post_id_to_be_returned
	return post_id_to_be_returned
	
	# number_of_posts = len(json_data["data"])
	# print 'blah'
	# for i in xrange(number_of_posts):
	# 	id = json_data["data"][i]["id"]
	# 	likes_on_post = get_number_of_likes_on_post(id)
		
	# 	return likes_on_post
		
	#generate access token via oauth, once done
	

# def get_data_from_page_id_posts():
# 	return "hello"

def get_data_from_post_id():
	# return "hello"
	url = 'https://graph.facebook.com/v2.2/116151972998/posts?access_token=CAACEdEose0cBAKTE1SgAIrAKkwi6WLMtg4QN28ZCkNDebFCZCK0c70MwEjnKIltZCJtz5PSJcZAzZC6zZAUx3p1sEkXzZCTkPTs92gb7bZCbIIgOThQwrWiTFkt1VcoTwCjibZBM6X89iNdjGBRI2aKw437kKkosVdBV44bVxJUUScuFdPCBcT6wWtqPZAhTuag1pmbZArS95I2KQwZATK1C77k4'
	json_data = connect_url(url)
	number_of_posts = len(json_data["data"])



def get_number_of_likes_on_post(id):
	# url = base_url + likes + ACCESS_TOKEN
	url = base_url + id + '/likes?access_token=' + ACCESS_TOKEN
	
	json_data = connect_url(url)
	length = len(json_data)
	data1 = json_data["data"]
	number_of_likes = len(data1)
	return number_of_likes
	# return number_of_likes

# def get_comment_count_on_post():
# 	url = 'https://graph.facebook.com/v2.2/116151972998_10153804678607999/comments?access_token=CAACEdEose0cBAE9nSzuhGXXQt8ZCycutnBq9JwlZA5tXImoShRbyDFa3LcxmVwpRVddbOEhYvHnVcf3Q6kndOe9pZBNplloeG1plM1viANggohdgmf8ALA0fefkiyZC8cm2TXSOmnmJe1Nqe8ElNWhY7yratd3SFraKKwQ6tQQ1mc0lP3tVAVsRkiTJYDeZAjs00DPOAkKwZDZD'
# 	response = requests.get(url)
# 	json_data = json.loads(response.text)
# 	number_of_comments = len(json_data["data"])
	

def get_author_name(id):
	# url = base_url + post + ACCESS_TOKEN
	url = 'https://graph.facebook.com/v2.2/' + id +'?access_token=CAACEdEose0cBAKTE1SgAIrAKkwi6WLMtg4QN28ZCkNDebFCZCK0c70MwEjnKIltZCJtz5PSJcZAzZC6zZAUx3p1sEkXzZCTkPTs92gb7bZCbIIgOThQwrWiTFkt1VcoTwCjibZBM6X89iNdjGBRI2aKw437kKkosVdBV44bVxJUUScuFdPCBcT6wWtqPZAhTuag1pmbZArS95I2KQwZATK1C77k4'
	json_data = connect_url(url)
	author_name = json_data["admin_creator"]["name"]
	# post_id = json_data["id"]
	title = json_data["name"]
	return title, author_name

def get_data_for_json(id):
	# url = base_url + post + ACCESS_TOKEN
	url = 'https://graph.facebook.com/v2.2/' + id +'?access_token=CAACEdEose0cBAKTE1SgAIrAKkwi6WLMtg4QN28ZCkNDebFCZCK0c70MwEjnKIltZCJtz5PSJcZAzZC6zZAUx3p1sEkXzZCTkPTs92gb7bZCbIIgOThQwrWiTFkt1VcoTwCjibZBM6X89iNdjGBRI2aKw437kKkosVdBV44bVxJUUScuFdPCBcT6wWtqPZAhTuag1pmbZArS95I2KQwZATK1C77k4'
	json_data = connect_url(url)
	author_name = json_data["admin_creator"]["name"]
	# post_id = id
	title = json_data["name"]
	return title, author_name

# def get_post_title(id):
# 	url = 'https://graph.facebook.com/v2.2/' + id +'?access_token=CAACEdEose0cBAE9nSzuhGXXQt8ZCycutnBq9JwlZA5tXImoShRbyDFa3LcxmVwpRVddbOEhYvHnVcf3Q6kndOe9pZBNplloeG1plM1viANggohdgmf8ALA0fefkiyZC8cm2TXSOmnmJe1Nqe8ElNWhY7yratd3SFraKKwQ6tQQ1mc0lP3tVAVsRkiTJYDeZAjs00DPOAkKwZDZD'
# 	# print url
# 	response = requests.get(url)
# 	json_data = json.loads(response.text)
# 	title = json_data["name"]
# 	return title	
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
def get_json_all(i):
	post_id = get_data_from_page_id(i)
		# print i, post_id
		# 
		# post_title, author = get_author_name(post_id)
	post_id = post_id
	post_title, author = get_author_name(post_id)
		# print post_id, post_title, author
	likes = get_number_of_likes_on_post(post_id) + i

		# data["post_id"] = post_id
		# print post_id
	data["post_id"] = post_id
	data["title"] = post_title		
	data["author_name"] = author
	data["likes"] = likes
	return data

# def json_data_test():
# 	for i in range(0,5):
# 		get_json_all(i)

		# print data1
		# print data["post_id"], data["title"], data["author_name"], data["likes"]
	# print data
	# print data1
	# json_data = json.loads(json.dumps(data1, ensure_ascii=False))
	# return json_data

	# data["post_id"]='aaa'
	# data['author_name'] = 'bbb'
	# print data
	# json_data1 = json.loads(json.dumps(data, ensure_ascii=False))
	# print json_data1
	# print json_data1["post_id"]
	# for i in range(0,25):
	# 	data["post_id"] = 
	# 	data["author_name"] =

	
# get_json_all()
# a, b = get_author_name('116151972998_10153811117102999')
# print a, b
# a = get_json_all()
# print a

def get_json_test():
	dict_test = []
	dict_test1 = {}
	c = ''
	for a in range(0,25):
		b = get_json_all(a)
		b = str(b)
		# c = c + ',' + b
		dict_test.append(b)
		# dict_test1.append(b)
		# dict_test.append(b)
		
	# dict_test.append(c)
	json_data1 = json.loads(json.dumps(dict_test, ensure_ascii=False))
	# print json_data1[0]
	# print ' '
	# print json_data1[1]
	# print ' '
	# print json_data1[2]
	return json_data1
	# json_data2 = json.loads(dict_test)
	# print dict_test1
	# print ''
	# print dict_test
	# print ' '
	# print json_data1
	# print json_data1[0], 'aaaaaaaaaaa', json_data1[1], 'bbbbbbbbbb', json_data1[2]
	# print json_data1
	# return json_data1

# def get_json_test():
# 	dict_test = []
# 	c = ''
# 	for a in range(10,25):
# 		b = get_json_all(a)
# 		b = str(b)
# 		c = c + ',' + b
# 		# dict_test.append(b)
		
# 	dict_test.append(c)
# 	json_data1 = json.loads(json.dumps(dict_test, ensure_ascii=False))
# 	return json_data1


# get_json_test()
# a = get_data_from_page_id(28)
# print a
# get_json_test()

#for the connection part
def connect_url(url):
	response = requests.get(url)
	json_data = json.loads(response.text)
	return json_data

# a = get_json_test()
# print a

def database_test():
	sqlite_file = '/home/puja/Documents/fb-api-test/fb-api.db'
	table_name1 = 'fb_api_test'

	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

	c.execute('CREATE TABLE IF NOT EXISTS fb_api_test (post_id integer, post_title text, author text, likes integer)')

	# post_id = 1234588
	# post_title = 'aaaaghaaaaaaabb'
	# author = 'dddgfdee'
	# likes = 14
	for i in range(1,25):
		post_id = get_data_from_page_id(i)
		post_title, author = get_author_name(post_id)
		likes = get_number_of_likes_on_post(post_id)

		c.execute("insert into fb_api_test(post_id, post_title, author, likes) values (?,?,?,?)",(post_id,post_title,author,likes))
		# c.execute("insert into fb_api_test(post_title) values (?)",(post_title,))
		# c.execute("insert into fb_api_test(author) values (?)",(author,))
		# c.execute("insert into fb_api_test(likes) values (?)",(likes,))

		
	conn.commit()
	conn.close()

database_test()
# def get_total_number_of_posts_on_page():
# 	url = 'https://graph.facebook.com/v2.2/116151972998/posts?access_token=CAACEdEose0cBAKTE1SgAIrAKkwi6WLMtg4QN28ZCkNDebFCZCK0c70MwEjnKIltZCJtz5PSJcZAzZC6zZAUx3p1sEkXzZCTkPTs92gb7bZCbIIgOThQwrWiTFkt1VcoTwCjibZBM6X89iNdjGBRI2aKw437kKkosVdBV44bVxJUUScuFdPCBcT6wWtqPZAhTuag1pmbZArS95I2KQwZATK1C77k4'
# 	posts_count = 0
# 	postsCount = postsCount + {the posts json array size}
