from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth
from flask_sqlalchemy import SQLAlchemy
import json
import requests
import sqlite3

post_id_array = ['116151972998_10153790740752999', '116151972998_10153790729467999', '116151972998_10153790734532999', '116151972998_10153790606757999', '116151972998_10153790725547999', '116151972998_10153790709802999', '116151972998_10153790612272999', '116151972998_10153790693552999',  '116151972998_10153790651222999', '116151972998_10153790617042999', '116151972998_10153790571787999', '116151972998_10153790566002999', '116151972998_10153790400547999', '116151972998_10153790502707999', '116151972998_10153790418377999', '116151972998_10153790413367999', '116151972998_10153790740752999', '116151972998_10153790729467999', '116151972998_10153790734532999', '116151972998_10153790606757999', '116151972998_10153790725547999', '116151972998_10153790709802999', '116151972998_10153790612272999', '116151972998_10153790693552999', '116151972998_10153790651222999', '116151972998_10153790617042999', '116151972998_10153790571787999']



def get_number_of_likes_on_post(id):
    # url = base_url + likes + ACCESS_TOKEN
    id1 = str(id)
    url = 'https://graph.facebook.com/v2.2/' + id1 +'/likes?access_token=CAACEdEose0cBAHikaxOhrSDfxtQWqaFvm5Y8z64HTZBbIcLIlZBW8ZA9VZCF4Q65rceanyG4wlij1fSsDEZBOgHa4o5wBxRiw5t6Pgm2AZBowB9FC3hkRBhNQSwdyuBy5iWYmQWcWXJgRw6CI9bNsWObZCUcvHcorOZB6YrWtuO4hxKZADZC3EQCWRvUBdsa7FHGaBRmHv9rDj3AZDZD'
    response = requests.get(url)
    json_data = json.loads(response.text)
    likes = json_data['data']
    next_url1 = json_data['paging']['next']
    next_url = []
    count = 1
    like_count = 0
    # print next_url1
    if json_data['paging'] and 'next' in json_data['paging'].keys():
        i = 1
    while(i):
        response = requests.get(next_url1)
        json_data = json.loads(response.text)
        likes = json_data['data']
        like_count = like_count + len(json_data['data'])
        if json_data['paging'] and 'next' in json_data['paging'].keys():
            next_url1 = json_data['paging']['next']
            i = 1
        else:
            i = 0
            # next_url1 = 'exit'
        # next_url.append(next_url1)
        # print i
        count = count+1
    # print count
    return like_count

def update_likes():
	sqlite_file = '/home/puja/Downloads/fb-api_500.db'
	table_name1 = 'fb_api_test'

	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

	# c.execute('CREATE TABLE IF NOT EXISTS fb_api_test (post_id integer, post_title text, author text, likes integer, post_link text, post_updated_time text)')

	# post_id = 1234588
	# post_title = 'aaaaghaaaaaaabb'
	# author = 'dddgfdee'
	# likes = 14
	for post_id in post_id_array:
		like = get_number_of_likes_on_post(post_id)
		likes = str(like)
		query = 'UPDATE fb_api_test SET likes=' + likes + ' WHERE post_id="' + post_id + '";'
		print query
	# i = 0
	# count1 = len(post_urls)
	# for i in range(1,count1):
	# for post_url in post_urls:
	# 	for i in range(0,25):
	# 		post_id = get_data_from_page_id(post_url, i)
	# 		post_title, author, link, time = get_author_name(post_id)
	# 		likes = get_number_of_likes_on_post(post_id)

	# 		c.execute("insert into fb_api_test(post_id, post_title, author, likes, post_link, post_updated_time) values (?,?,?,?,?,?)",(post_id, post_title, author, likes, link, time))
def get_likes_1275():
    sqlite_file = '/home/puja/Downloads/fb-api_500_data.db'
    table_name1 = 'fb_api_test'

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    # c.execute('CREATE TABLE IF NOT EXISTS fb_api_test (post_id integer, post_title text, author text, likes integer, post_link text, post_updated_time text)')

    # post_id = 1234588
    # post_title = 'aaaaghaaaaaaabb'
    # author = 'dddgfdee'
    # likes = 14
    array = []
    query= "select post_id from fb_api_test where likes=1275"
    c.execute(query)
    results = c.fetchall()
    for result in results:
        array.append(result)
    print array

# get_likes_1275()
update_likes()