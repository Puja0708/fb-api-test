from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth
from flask_sqlalchemy import SQLAlchemy
import json
import requests


ACCESS_TOKEN = 'CAACEdEose0cBANXHOluTccNW8WoPZCRWr6EtRw7LEo4GCX4D7NYwZB3U25NBGFsxVU95IJly3IXDNZBE6ZAmSUwEfclHqqIBLhGMnytbrDxSqSb4oQOoWi8QsduyC4IPjwz1ZAMTF0l2wb9oAE9xmHWu6scGK3pro7rGAZBRWLcyM5JTW8WyHMSaIwh4qksavyIcL4nKdEZBgZDZD'
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
	
	url = 'https://graph.facebook.com/v2.2/116151972998/posts?access_token=CAACEdEose0cBANXHOluTccNW8WoPZCRWr6EtRw7LEo4GCX4D7NYwZB3U25NBGFsxVU95IJly3IXDNZBE6ZAmSUwEfclHqqIBLhGMnytbrDxSqSb4oQOoWi8QsduyC4IPjwz1ZAMTF0l2wb9oAE9xmHWu6scGK3pro7rGAZBRWLcyM5JTW8WyHMSaIwh4qksavyIcL4nKdEZBgZDZD'
	response = requests.get(url)
	json_data = json.loads(response.text)
	data1 = json_data["data"]
		# post_id_to_be_returned = data1[i]["id"]
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
	url = 'https://graph.facebook.com/v2.2/116151972998/posts?access_token=CAACEdEose0cBANXHOluTccNW8WoPZCRWr6EtRw7LEo4GCX4D7NYwZB3U25NBGFsxVU95IJly3IXDNZBE6ZAmSUwEfclHqqIBLhGMnytbrDxSqSb4oQOoWi8QsduyC4IPjwz1ZAMTF0l2wb9oAE9xmHWu6scGK3pro7rGAZBRWLcyM5JTW8WyHMSaIwh4qksavyIcL4nKdEZBgZDZD'
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

# def get_comment_count_on_post():
# 	url = 'https://graph.facebook.com/v2.2/116151972998_10153804678607999/comments?access_token=CAACEdEose0cBAE9nSzuhGXXQt8ZCycutnBq9JwlZA5tXImoShRbyDFa3LcxmVwpRVddbOEhYvHnVcf3Q6kndOe9pZBNplloeG1plM1viANggohdgmf8ALA0fefkiyZC8cm2TXSOmnmJe1Nqe8ElNWhY7yratd3SFraKKwQ6tQQ1mc0lP3tVAVsRkiTJYDeZAjs00DPOAkKwZDZD'
# 	response = requests.get(url)
# 	json_data = json.loads(response.text)
# 	number_of_comments = len(json_data["data"])
	

def get_author_name(id):
	# url = base_url + post + ACCESS_TOKEN
	url = 'https://graph.facebook.com/v2.2/' + id +'?access_token=CAACEdEose0cBANXHOluTccNW8WoPZCRWr6EtRw7LEo4GCX4D7NYwZB3U25NBGFsxVU95IJly3IXDNZBE6ZAmSUwEfclHqqIBLhGMnytbrDxSqSb4oQOoWi8QsduyC4IPjwz1ZAMTF0l2wb9oAE9xmHWu6scGK3pro7rGAZBRWLcyM5JTW8WyHMSaIwh4qksavyIcL4nKdEZBgZDZD'
	response = requests.get(url)
	json_data = json.loads(response.text)
	author_name = json_data["admin_creator"]["name"]
	# post_id = json_data["id"]
	title = json_data["name"]
	return title, author_name

def get_data_for_json(id):
	# url = base_url + post + ACCESS_TOKEN
	url = 'https://graph.facebook.com/v2.2/' + id +'?access_token=CAACEdEose0cBANXHOluTccNW8WoPZCRWr6EtRw7LEo4GCX4D7NYwZB3U25NBGFsxVU95IJly3IXDNZBE6ZAmSUwEfclHqqIBLhGMnytbrDxSqSb4oQOoWi8QsduyC4IPjwz1ZAMTF0l2wb9oAE9xmHWu6scGK3pro7rGAZBRWLcyM5JTW8WyHMSaIwh4qksavyIcL4nKdEZBgZDZD'
	response = requests.get(url)
	json_data = json.loads(response.text)
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
	c = ''
	for a in range(0,10):
		b = get_json_all(a)
		b = str(b)
		c = c + ',' + b
		# dict_test.append(b)
		
	dict_test.append(c)
	json_data1 = json.loads(json.dumps(dict_test, ensure_ascii=False))
	return json_data1

def get_json_test():
	dict_test = []
	c = ''
	for a in range(10,25):
		b = get_json_all(a)
		b = str(b)
		c = c + ',' + b
		# dict_test.append(b)
		
	dict_test.append(c)
	json_data1 = json.loads(json.dumps(dict_test, ensure_ascii=False))
	return json_data1


# get_json_test()
a = get_data_from_page_id(28)
print a