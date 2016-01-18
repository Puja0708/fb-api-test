import MySQLdb as dbapi
import sys
import csv
import json
import requests

# dbServer='localhost'
# dbPass='supersecretpassword'
# dbSchema='dbTest'
# dbUser='root'
api_endpoint = 'api.sportskeeda.com/v1/author/'
dbServer='localhost'
dbPass=''
dbSchema='sportskeeda'
dbUser='sportskeeda'
database_location="/var/lib/mysql/sportskeeda"
conn = dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass,db="sportskeeda")
c = conn.cursor()
# print "done"

dbQuery = "SELECT distinct author_id FROM keeda_author_fact  ORDER BY author_post_count DESC LIMIT 5;"
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
print authors_final
for ids in authors_final:
	url_to_hit = api_endpoint + ids
	# print url_to_hit
	api_array.append(url_to_hit)
	# response = requests.get(url_to_hit)
	# print "foo"
	# json_data = (response.text)
	# print json_data
print api_array

for url in api_array:
	url1 = str(url)
	url1.replace("'","")
	print url1
	response = requests.request("GET", url1)
	print "foo"


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