from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth
from flask_sqlalchemy import SQLAlchemy
import json
import requests
import sqlite3
import csv

def database_test():
	sqlite_file = '/home/puja/Downloads/fb-api_500_data.db'
	table_name1 = 'fb_api_test'

	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	authors = ['Saransh Gehlot', 'Vignesh Madridista Ananthasubramanian', 'Khushwant Ramesh', 'Foma Ramteke', 'Anuradha Santhanam', 'Shankar Narayan V', 'Nitin Fernandes', 'Rohith Nair', 'Siddarth Sharma', 'Shubham Mazumdar', 'Absolute Sports PVt. Ltd', 'Sri Hari', 'Vinay Sundar', 'Akash Iyer', 'Pritam Sharma', 'Ratish Menon', 'Dipankar Lahiri']
	with open('/home/puja/Documents/fb-api-test/fb-report.csv', 'a') as outfile:
		writer = csv.writer(outfile)
		i = 0
	for author in authors:
		query = "SELECT * FROM fb_api_test WHERE author='" + 'Dipankar Lahiri' + "';"
		# print query
		c.execute(query)
		results = c.fetchall()
		new_file = 'report_author' + str(i)
		# print new_file
		new_file = []
		big_data_file = []
		for result in results:
			# print result
			new_file.append(result)
	with open('/home/puja/Documents/fb-api-test/fb-report16.csv', 'a') as outfile:
		a = csv.writer(outfile, delimiter=',')
		data = results
		a.writerows(data)

# 		select count(post_id) from fb_api_test where author="Dipankar Lahiri" and post_link LIKE "%www.sportskeeda.com%";

# select count(post_id) from fb_api_test where author="Dipankar Lahiri" and post_link NOT LIKE "%www.sportskeeda.com%";

# select SUM(likes) from fb_api_test where author="Dipankar Lahiri" and post_link LIKE "%www.sportskeeda.com%";

# select SUM(likes) from fb_api_test where author="Dipankar Lahiri" and post_link NOT LIKE "%www.sportskeeda.com%";




		# print new_file
		# big_data_file.append(new_file)

		# print big_data_file
		# print len(big_data_file)

			# with open('/home/puja/Documents/fb-api-test/fb-report.csv', 'a') as outfile:
			# 	writer = csv.writer(outfile)
			# 	writer.writerow(result)
			# 	print "done"
		# for result in results:
		# 	with open('/home/puja/Documents/fb-api-test/fb-report.csv', 'a') as outfile:
		# 		writer = csv.writer(outfile)
		# 		writer.writerow(result)


	# c.execute('SELECT DISTINCT author from fb_api_test;')
	# results = c.fetchall()
	# authors = []
	# for result in results:
	# 	authors.append(result)
	# print authors
	# post_id = 1234588
	# post_title = 'aaaaghaaaaaaabb'
	# author = 'dddgfdee'
	# likes = 14
	
		# c.execute("insert into fb_api_test(post_title) values (?)",(post_title,))
		# c.execute("insert into fb_api_test(author) values (?)",(author,))
		# c.execute("insert into fb_api_test(likes) values (?)",(likes,))
			

	conn.commit()
	conn.close()
	print "done"
database_test()