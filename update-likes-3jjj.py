from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth
from flask_sqlalchemy import SQLAlchemy
import json
import requests
import sqlite3

post_id_array = ['116151972998_10153825936217999', '116151972998_10153825820097999', '116151972998_10153825657772999', '116151972998_10153825643037999', '116151972998_10153825625702999', '116151972998_10153825582932999', '116151972998_10153824936277999', '116151972998_10153825450577999', '116151972998_10153825538602999', '116151972998_10153825503532999', '116151972998_10153825467087999', '116151972998_10153825406677999', '116151972998_10153825408542999', '116151972998_10153825368092999', '116151972998_10153825327337999', '116151972998_10153825262952999', '116151972998_10153825191982999', '116151972998_10153825112402999', '116151972998_10153824962032999', '116151972998_10153824954227999', '116151972998_10153824864887999', '116151972998_10153824659987999', '116151972998_10153824616342999', '116151972998_10153824593292999', '116151972998_10153824660542999', '116151972998_10153824476352999', '116151972998_10153824574362999', '116151972998_10153824540407999', '116151972998_10153824496862999', '116151972998_10153824487997999', '116151972998_10153824446802999', '116151972998_10153824429222999', '116151972998_10153824418487999', '116151972998_10153824377187999', '116151972998_10153824357672999', '116151972998_10153824326097999', '116151972998_10153824328887999', '116151972998_10153823390632999', '116151972998_10153823604807999', '116151972998_10153823215737999', '116151972998_10153823190462999', '116151972998_10153823103972999', '116151972998_10153823083957999', '116151972998_10153823066602999', '116151972998_10153822890682999', '116151972998_10153822911352999', '116151972998_10153822947467999', '116151972998_10153822894752999', '116151972998_10153822901212999', '116151972998_10153822797917999', '116151972998_10153822781602999', '116151972998_10153822753582999', '116151972998_10153822730627999', '116151972998_10153822498657999', '116151972998_10153822663342999', '116151972998_10153822644937999', '116151972998_10153822613632999', '116151972998_10153822588682999', '116151972998_10153822300852999', '116151972998_10153822553102999', '116151972998_10153822510207999', '116151972998_10153822518067999', '116151972998_10153822500112999', '116151972998_10153822472707999', '116151972998_10153822453522999', '116151972998_10153822437182999', '116151972998_10153822382027999', '116151972998_10153822367112999', '116151972998_10153822329907999', '116151972998_10153822273592999', '116151972998_10153822239807999', '116151972998_10153822140737999', '116151972998_10153822097832999', '116151972998_10153822073682999', '116151972998_10153822058282999', '116151972998_10153822043157999', '116151972998_10153822019832999', '116151972998_10153821969167999', '116151972998_10153821946987999', '116151972998_10153821915622999', ]



def get_number_of_likes_on_post(id):
    # url = base_url + likes + ACCESS_TOKEN
    id1 = str(id)
    url = 'https://graph.facebook.com/v2.2/' + id1 +'/likes?access_token=CAACEdEose0cBANQP8FAJDg3o1KVZAZBRwAWktvajoQcoKZB2gF5MdDZCK8U10udA6ehgaf5bo2uGcUm74k7nfb8TruLayVH9WVV9rUqYOc5XltaUmQ9IHinj3L9eMVDhqJuFJndKN6dAQdnZCwrwjFp0ZA2M20GNINnPaH3LIhqNRbMZAZAlGPZCsHnORe6FtT94yZC8wGelFLMgZDZD'
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

get_likes_1275()
# update_likes()