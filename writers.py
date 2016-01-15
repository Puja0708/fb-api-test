import MySQLdb
import json

DEBUG = True
database_location = '/var/lib/mysql/'
table_name = 'keeda_author_fact'
db = MySQLdb.connect('localhost', 'sportskeeda', '', 'sportskeeda')
query = 'select author_id, author_url, author_title, author_post_count, total_reads, author_rss from keeda_author_fact ORDER BY author_post_count limit 20'
# ?dbconfig = read_db_config()
# conn = MySQLConnection(**dbconfig)
cursor = db.cursor()
cursor.execute(query)
rows = cursor.fetchall()
json_data = []
for row in rows:
	json_data.append(row)

json_data1 = json.dumps(json_data)

# print rows
print json_data, json_data[0]