from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth
from flask_sqlalchemy import SQLAlchemy
import json
import requests
import sqlite3








ACCESS_TOKEN = 'CAACEdEose0cBAOaVxWbj6ZAEvZAuuB4jtQB1iWBHUJlqLnSeSZChfa7jSLyhOJ0b6aAZABLLTWIcOBssxMaqw5WxktZBU19I3jKUXhdMBzLPsiYhZAMEgCUQkTdkktELAvGXB72vidjuuThW3ZCaDPK5D9n2v5j0ZB2MUBngnF88n1BUHblq5M3IVq7lB07G6rDRHj99IHHY3CR1gWERHjcv'
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

post_urls=['https://graph.facebook.com/v2.2/116151972998/posts?limit=25&__paging_token=enc_AdA3CLIwZBCJLuTek2P1DMJM9SXt5xp3Ye5TYQZAqDSrBgoAOMOSmqA0f69XtdY4wLFgfuCgiJeVO0ETihhDQh2EihZBkLjVeQg051D2ykYpu8BNwZDZD&access_token=CAACEdEose0cBABL3qKfnZCa4CauG8xga8G0SJboD1vr2pEXQudbZBNJgqwsP1WRMQR9HITYVc3ZBdSNygZAarCgYbY87ygXS2xH2Ju2OZBpJjVZAfzgPwGh9XnecAs0DUHeKKiWAmXXMqll95raZAUjsJT61rJlMRRZBlNy34G7itBnst6r4nByt1fSkey4e4MLMBARATJEZCg8ZBkMxp3gOVM&until=1452711835', 'https://graph.facebook.com/v2.2/116151972998/posts?limit=25&__paging_token=enc_AdDKbrrnMtVUWO9Hozbh5RVFHuYpEC8pWcERXPs9wpsWuyWMjmgsgo8fstV4PfsbguBaMlvt3CEmnPUtvZA5GEMI5iGIeci9WzvBTyYDZAE2tC2gZDZD&access_token=CAACEdEose0cBABL3qKfnZCa4CauG8xga8G0SJboD1vr2pEXQudbZBNJgqwsP1WRMQR9HITYVc3ZBdSNygZAarCgYbY87ygXS2xH2Ju2OZBpJjVZAfzgPwGh9XnecAs0DUHeKKiWAmXXMqll95raZAUjsJT61rJlMRRZBlNy34G7itBnst6r4nByt1fSkey4e4MLMBARATJEZCg8ZBkMxp3gOVM&until=1452691879', 'https://graph.facebook.com/v2.2/116151972998/posts?limit=25&__paging_token=enc_AdBiWwwJbAZBYuv49gAjvJJYwqSdZCwOTwOWA7JoR4OOSvdeZB6eVzEnpoPYLZBdJpXOBCCGhhzaxPNiLHYn55ahXZCc9ep8NxAClHUmLmfkxs0qODAZDZD&access_token=CAACEdEose0cBABL3qKfnZCa4CauG8xga8G0SJboD1vr2pEXQudbZBNJgqwsP1WRMQR9HITYVc3ZBdSNygZAarCgYbY87ygXS2xH2Ju2OZBpJjVZAfzgPwGh9XnecAs0DUHeKKiWAmXXMqll95raZAUjsJT61rJlMRRZBlNy34G7itBnst6r4nByt1fSkey4e4MLMBARATJEZCg8ZBkMxp3gOVM&until=1452671012', 'https://graph.facebook.com/v2.2/116151972998/posts?limit=25&__paging_token=enc_AdAqbHZAtW3Se36AWc9WbL8HzlI7qCkiNB4EJAB9o1XDF7rjFS11fNk0OaGxc9ZByE3JsIqJWMz0Mtvv12B1xINSPfCCqaxkgjggwe5VhyWYsf1wZDZD&access_token=CAACEdEose0cBABL3qKfnZCa4CauG8xga8G0SJboD1vr2pEXQudbZBNJgqwsP1WRMQR9HITYVc3ZBdSNygZAarCgYbY87ygXS2xH2Ju2OZBpJjVZAfzgPwGh9XnecAs0DUHeKKiWAmXXMqll95raZAUjsJT61rJlMRRZBlNy34G7itBnst6r4nByt1fSkey4e4MLMBARATJEZCg8ZBkMxp3gOVM&until=1452622077', 'https://graph.facebook.com/v2.2/116151972998/posts?limit=25&__paging_token=enc_AdBCwjTb6wrs9w07B7PgIUcGvZCmSH3tY5P3qndtYbWJD1bpzJM2KHDhWlnvtWDnbDqKaqmxGrQdfnmf5XR5jxwlZB3qLkCaVZAwEc3s5HNl8eUyAZDZD&access_token=CAACEdEose0cBABL3qKfnZCa4CauG8xga8G0SJboD1vr2pEXQudbZBNJgqwsP1WRMQR9HITYVc3ZBdSNygZAarCgYbY87ygXS2xH2Ju2OZBpJjVZAfzgPwGh9XnecAs0DUHeKKiWAmXXMqll95raZAUjsJT61rJlMRRZBlNy34G7itBnst6r4nByt1fSkey4e4MLMBARATJEZCg8ZBkMxp3gOVM&until=1452601212', 'https://graph.facebook.com/v2.2/116151972998/posts?limit=25&__paging_token=enc_AdDlYHg61Ee3jMOpjN3FAVoDXvMOvaOCCRytGkKsgWxWw3M1lJ01fMNx6PLogstmpYAd2xAakQB26dVPFyCZAqC7TQQHK8f6tJFCXRQs4Wq9iiQZDZD&access_token=CAACEdEose0cBABL3qKfnZCa4CauG8xga8G0SJboD1vr2pEXQudbZBNJgqwsP1WRMQR9HITYVc3ZBdSNygZAarCgYbY87ygXS2xH2Ju2OZBpJjVZAfzgPwGh9XnecAs0DUHeKKiWAmXXMqll95raZAUjsJT61rJlMRRZBlNy34G7itBnst6r4nByt1fSkey4e4MLMBARATJEZCg8ZBkMxp3gOVM&until=1452577187', 'https://graph.facebook.com/v2.2/116151972998/posts?limit=25&__paging_token=enc_AdCN0m9MF1SIr5lPRKsZCWsWZC97O2dmnbNT6VzTEVpaiE8rhk6b0obELZCQYVienAafS9B4HJuxLctUgmdT7ChHzWHZBZCoIu4PXsXaQkWyTG6sOygZDZD&access_token=CAACEdEose0cBABL3qKfnZCa4CauG8xga8G0SJboD1vr2pEXQudbZBNJgqwsP1WRMQR9HITYVc3ZBdSNygZAarCgYbY87ygXS2xH2Ju2OZBpJjVZAfzgPwGh9XnecAs0DUHeKKiWAmXXMqll95raZAUjsJT61rJlMRRZBlNy34G7itBnst6r4nByt1fSkey4e4MLMBARATJEZCg8ZBkMxp3gOVM&until=1452535160', 'https://graph.facebook.com/v2.2/116151972998/posts?limit=25&__paging_token=enc_AdDEWRfx7eAM2BaP6tPqzZCX1LZB8TOU37yqxo4r2Bm5sCvd4VMmgZC8iSIjZCj3eepABP4cZAIJSRFBnPPcQjTRNBVksekZBCDNNIX1cZAq7L3J94chAZDZD&access_token=CAACEdEose0cBABL3qKfnZCa4CauG8xga8G0SJboD1vr2pEXQudbZBNJgqwsP1WRMQR9HITYVc3ZBdSNygZAarCgYbY87ygXS2xH2Ju2OZBpJjVZAfzgPwGh9XnecAs0DUHeKKiWAmXXMqll95raZAUjsJT61rJlMRRZBlNy34G7itBnst6r4nByt1fSkey4e4MLMBARATJEZCg8ZBkMxp3gOVM&until=1452519420', 'https://graph.facebook.com/v2.2/116151972998/posts?limit=25&__paging_token=enc_AdBnTS01yxKX6pXnDYXglPIZCHbwNLh6cFKXOOqiIEZC0dBZAxQ2Rk3Gg84XcLJf32DZCw0dFkQ1suSQWenoqoCGK1ZCTTkjFjG5N6VW6FwqCjjk2uAZDZD&access_token=CAACEdEose0cBABL3qKfnZCa4CauG8xga8G0SJboD1vr2pEXQudbZBNJgqwsP1WRMQR9HITYVc3ZBdSNygZAarCgYbY87ygXS2xH2Ju2OZBpJjVZAfzgPwGh9XnecAs0DUHeKKiWAmXXMqll95raZAUjsJT61rJlMRRZBlNy34G7itBnst6r4nByt1fSkey4e4MLMBARATJEZCg8ZBkMxp3gOVM&until=1452499503', 'https://graph.facebook.com/v2.2/116151972998/posts?limit=25&__paging_token=enc_AdDhefyVXQ3vDXwspezwIqjXWrTjLOfS1eUoZCrT6NOcDRIErluVfBUAgUow4GjlJpkQAaEPEexoXINZCjF0fV8yVgaqZChdAngZBlZCTDQPUkzTZBTQZDZD&access_token=CAACEdEose0cBABL3qKfnZCa4CauG8xga8G0SJboD1vr2pEXQudbZBNJgqwsP1WRMQR9HITYVc3ZBdSNygZAarCgYbY87ygXS2xH2Ju2OZBpJjVZAfzgPwGh9XnecAs0DUHeKKiWAmXXMqll95raZAUjsJT61rJlMRRZBlNy34G7itBnst6r4nByt1fSkey4e4MLMBARATJEZCg8ZBkMxp3gOVM&until=1452449160']

#we are using the facebook graph API version 2.2, instead of the latest one(2.5)
def get_data_from_page_id(url,i):
	
	url = url
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
	url = 'https://graph.facebook.com/v2.2/116151972998/posts?access_token=CAACEdEose0cBAOaVxWbj6ZAEvZAuuB4jtQB1iWBHUJlqLnSeSZChfa7jSLyhOJ0b6aAZABLLTWIcOBssxMaqw5WxktZBU19I3jKUXhdMBzLPsiYhZAMEgCUQkTdkktELAvGXB72vidjuuThW3ZCaDPK5D9n2v5j0ZB2MUBngnF88n1BUHblq5M3IVq7lB07G6rDRHj99IHHY3CR1gWERHjcv'
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
	url = 'https://graph.facebook.com/v2.2/' + id +'?access_token=CAACEdEose0cBAOaVxWbj6ZAEvZAuuB4jtQB1iWBHUJlqLnSeSZChfa7jSLyhOJ0b6aAZABLLTWIcOBssxMaqw5WxktZBU19I3jKUXhdMBzLPsiYhZAMEgCUQkTdkktELAvGXB72vidjuuThW3ZCaDPK5D9n2v5j0ZB2MUBngnF88n1BUHblq5M3IVq7lB07G6rDRHj99IHHY3CR1gWERHjcv'
	json_data = connect_url(url)
	author_name = json_data["admin_creator"]["name"]
	# post_id = json_data["id"]
	title = json_data["name"]
	link = json_data["link"]
	updated_time = json_data["updated_time"]
	return title, author_name, link, updated_time

def get_data_for_json(id):
	# url = base_url + post + ACCESS_TOKEN
	url = 'https://graph.facebook.com/v2.2/' + id +'?access_token=CAACEdEose0cBAOaVxWbj6ZAEvZAuuB4jtQB1iWBHUJlqLnSeSZChfa7jSLyhOJ0b6aAZABLLTWIcOBssxMaqw5WxktZBU19I3jKUXhdMBzLPsiYhZAMEgCUQkTdkktELAvGXB72vidjuuThW3ZCaDPK5D9n2v5j0ZB2MUBngnF88n1BUHblq5M3IVq7lB07G6rDRHj99IHHY3CR1gWERHjcv'
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
	post_title, author, link, updated_time = get_author_name(post_id)
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

	c.execute('CREATE TABLE IF NOT EXISTS fb_api_test (post_id integer, post_title text, author text, likes integer, post_link text, post_updated_time text)')

	# post_id = 1234588
	# post_title = 'aaaaghaaaaaaabb'
	# author = 'dddgfdee'
	# likes = 14
	i = 0
	count1 = len(post_urls)
	# for i in range(1,count1):
	for post_url in post_urls:
		for i in range(0,25):
			post_id = get_data_from_page_id(post_url, i)
			post_title, author, link, time = get_author_name(post_id)
			likes = get_number_of_likes_on_post(post_id)

			c.execute("insert into fb_api_test(post_id, post_title, author, likes, post_link, post_updated_time) values (?,?,?,?,?,?)",(post_id, post_title, author, likes, link, time))
		# c.execute("insert into fb_api_test(post_title) values (?)",(post_title,))
		# c.execute("insert into fb_api_test(author) values (?)",(author,))
		# c.execute("insert into fb_api_test(likes) values (?)",(likes,))
			

	conn.commit()
	conn.close()
	print "done"

def get_all_posts():
	url = 'https://graph.facebook.com/v2.2/116151972998/posts?access_token=CAACEdEose0cBAOaVxWbj6ZAEvZAuuB4jtQB1iWBHUJlqLnSeSZChfa7jSLyhOJ0b6aAZABLLTWIcOBssxMaqw5WxktZBU19I3jKUXhdMBzLPsiYhZAMEgCUQkTdkktELAvGXB72vidjuuThW3ZCaDPK5D9n2v5j0ZB2MUBngnF88n1BUHblq5M3IVq7lB07G6rDRHj99IHHY3CR1gWERHjcv'
	# response = requests.get(url)
	all_posts = []
	count = 0
	posts = connect_url(url)
	while(posts['data']):
		for post in posts['data']:
			# all_posts.append(post['id'])
			count = count + 1
		url_next = posts['paging']['next']
		post_data = connect_url(url_next)
	print count

def get_likes_count():
	url = 'https://graph.facebook.com/v2.2/116151972998_10153825139507999/likes?access_token=CAACEdEose0cBAOaVxWbj6ZAEvZAuuB4jtQB1iWBHUJlqLnSeSZChfa7jSLyhOJ0b6aAZABLLTWIcOBssxMaqw5WxktZBU19I3jKUXhdMBzLPsiYhZAMEgCUQkTdkktELAvGXB72vidjuuThW3ZCaDPK5D9n2v5j0ZB2MUBngnF88n1BUHblq5M3IVq7lB07G6rDRHj99IHHY3CR1gWERHjcv'
	
	# likes = []
	likes_count = 1
	likes = connect_url(url)
	url_next = likes['paging']['next']
	# while(likes['data']):
	# 	print "foo"
	# print likes['data']
	# for i in range(0,4):
	# if(likes['data']):
	while(likes['data']):
		print "inside loop"
		for like in likes['data']:
			likes_count = likes_count + 1
		url_next = likes['paging']['next']
		likes_data = connect_url(url_next)
		likes['data'] = likes_data['data']
	print likes_count

def fb_paging_test():
	# url = 'https://graph.facebook.com/v2.2/116151972998_10153825139507999/likes?access_token=CAACEdEose0cBAOGlgBlnDPbqA0dhsfwzfdPSZAydk47EqOu4axjOV7ddiR4aUhVP8XU7ZC4SIqyqZCg6zFIyZBPpaJvFL9Ji91mG9LFzmyW9Bc8smmxJ9RYOxcsAaPViM426WraqY5I7L8148xGv7inItQmDxvtPTEiZA7TAULrwccxWOoOfTZCLazP2kd7oqK8CXqKUYhlgZDZD'
	url = 'https://graph.facebook.com/v2.2/116151972998/posts?access_token=CAACEdEose0cBAOaVxWbj6ZAEvZAuuB4jtQB1iWBHUJlqLnSeSZChfa7jSLyhOJ0b6aAZABLLTWIcOBssxMaqw5WxktZBU19I3jKUXhdMBzLPsiYhZAMEgCUQkTdkktELAvGXB72vidjuuThW3ZCaDPK5D9n2v5j0ZB2MUBngnF88n1BUHblq5M3IVq7lB07G6rDRHj99IHHY3CR1gWERHjcv'
	response = requests.get(url)
	json_data = json.loads(response.text)
	likes = json_data['data']
	next_url1 = json_data['paging']['next']
	next_url = []
	count = 1
	# print next_url1
	if json_data['paging'] and 'next' in json_data['paging'].keys() and count<51:
		i = 1
	while(i):
		response = requests.get(next_url1)
		json_data = json.loads(response.text)
		likes = json_data['data']	
		if json_data['paging'] and 'next' in json_data['paging'].keys() and count<51:
			next_url1 = json_data['paging']['next']
			i = 1
		else:
			i = 0
			next_url1 = 'exit'
		next_url.append(next_url1)
		print i
		count = count+1
	print next_url, count


	

database_test()

# def get_total_number_of_posts_on_page():
# 	url = 'https://graph.facebook.com/v2.2/116151972998/posts?access_token=CAACEdEose0cBAKTE1SgAIrAKkwi6WLMtg4QN28ZCkNDebFCZCK0c70MwEjnKIltZCJtz5PSJcZAzZC6zZAUx3p1sEkXzZCTkPTs92gb7bZCbIIgOThQwrWiTFkt1VcoTwCjibZBM6X89iNdjGBRI2aKw437kKkosVdBV44bVxJUUScuFdPCBcT6wWtqPZAhTuag1pmbZArS95I2KQwZATK1C77k4'
# 	posts_count = 0
# 	postsCount = postsCount + {the posts json array size}
