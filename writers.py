import MySQLdb as dbapi
import sys
import csv
import json
import requests
import urllib2

# dbServer='localhost'
# dbPass='supersecretpassword'
# dbSchema='dbTest'
# dbUser='root'
api_endpoint = 'http://puja_api.sportskeeda.com/v1/author/'
dbServer='localhost'
dbPass=''
dbSchema='sportskeeda'
dbUser='sportskeeda'
database_location="/var/lib/mysql/sportskeeda"
conn = dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass,db="sportskeeda")
c = conn.cursor()
# print "done"

dbQuery = "SELECT distinct author_id FROM keeda_author_fact  ORDER BY author_post_count DESC LIMIT 15941,50000;"
c.execute(dbQuery)
results = c.fetchall()

authors = []
authors_final = []
api_array = []
for result in results:

	authors.append(result)
for author in authors:
	author1 = str(author)
	auth = author1.split(',')
	auth2 = auth[0].split('(')[1]
	# print auth2
	authors_final.append(auth2)
# print authors_final
# with open('/home/puja/Documents/fb-api-test/test.csv', 'w') as outfile:
# 	writer = csv.writer(outfile)
# 	writer.writerow(['Author Id', 'author email', 'author nicename', 'posts published', 'reads received', 'editors pick', 'last published date'])
for ids in authors_final:
	url_to_hit = api_endpoint + ids
	url_to_hit_2 = "http://puja_api.sportskeeda.com/v1/author_posts/" + ids
	# print url_to_hit
	# response = urllib2.urlopen('api.sportskeeda.com/v1/author/4390L')
	# data = json.load(response) 
	response = requests.get(url_to_hit)
	json_data = json.loads(response.text)
	response2 =  requests.get(url_to_hit_2)
	json_data2 = json.loads(response2.text)
	# print json_data["fan_title"]
	author_id = ids
	if 'user_email' in json_data.keys():
		user_email = json_data["user_email"]
	else:
		user_email = ' '
	if 'user_nicename' in json_data.keys():
		user_nicename = json_data["user_nicename"]
	else:
		user_nicename = ' '
	if 'author_url' in json_data.keys():
		author_url = json_data["author_url"]
	else:
		author_url = ' '
	if 'posts_published' in json_data.keys():
		posts_published = json_data["posts_published"]
	else:
		posts_published = 0
	if 'editors_pick' in json_data.keys():
		editors_pick = json_data["editors_pick"]
	else:
		editors_pick = 0
	if 'reads_received' in json_data.keys():
		reads_received = json_data["reads_received"]
	else:
		reads_received = 0
	# if "post_date_formatted" in json_data2[0].keys():
	# print json_data2[0]
	count = len(json_data2)
	# print count
	if count>0:
		if json_data2[0] and 'post_date_formatted' in json_data2[0].keys():
			last_published_date = json_data2[0]["post_date_formatted"]
	else:
		print "foo"
		last_published_date = 0
	print user_email, user_nicename, posts_published, reads_received, editors_pick, last_published_date
	with open('/home/puja/Documents/fb-api-test/test.csv', 'a') as outfile:
		writer = csv.writer(outfile)
		writer.writerow([author_id, user_email, user_nicename, author_url, posts_published, editors_pick, reads_received, last_published_date])
	# fields = ['Author Id', 'post count','total reads', 'points(includes editors picks)', 'author name', 'author email']
	# writer = csv.DictWriter(outfile)
	
	# writer.writeheader()
	# for x in result:
	# 	writer.writerow(x)
def get_all_author_ids():
	bServer='localhost'
	dbPass=''
	dbSchema='sportskeeda'
	dbUser='sportskeeda'
	database_location="/var/lib/mysql/sportskeeda"
	conn = dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass,db="sportskeeda")
	c = conn.cursor()
	# print "done"
	array = []
	dbQuery = "SELECT distinct author_id FROM keeda_author_fact  ORDER BY author_post_count DESC LIMIT 10;"
	c.execute(dbQuery)
	results = c.fetchall()
	while result in results:
		array.append(result)
	print array

def get_all_data_from_db():
	bServer='localhost'
	dbPass=''
	dbSchema='sportskeeda'
	dbUser='sportskeeda'
	database_location="/var/lib/mysql/sportskeeda"
	conn = dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass,db="sportskeeda")
	c = conn.cursor()



# get_all_author_ids()
print "done"
















	# print url_to_hit
	# api_array.append(url_to_hit)
	# response = requests.get(url_to_hit)
	# print "foo"
	# json_data = (response.text)
	# print json_data

# outfile = open( "/home/puja/Documents/fb-api-test", "w" )

# writer = csv.writer( outfile )

# write header
 


# with open('/home/puja/Documents/fb-api-test/test.csv', 'w') as outfile:
# 	# fields = ['Author Id', 'post count','total reads', 'points(includes editors picks)', 'author name', 'author email']
# 	# writer = csv.DictWriter(outfile)
# 	writer = csv.writer(outfile)
# 	writer.writerow(['Author Id', 'post count','total reads', 'points(includes editors picks)', 'author name', 'author email'])
# 	# writer.writeheader()
# 	for x in result:
# 		writer.writerow(x)
# 	print "done"