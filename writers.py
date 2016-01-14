import MySQLdb

DEBUG = True
database_location = '/var/lib/mysql/'
table_name = 'keeda_author_fact'
db = MySQLdb.connect('localhost', 'sportskeeda', '', 'sportskeeda')
query = 'select author_id, author_url, author_title, author_post_count, total_reads, author_rss from keeda_author_fact ORDER BY author_post_count limit 5'
# ?dbconfig = read_db_config()
# conn = MySQLConnection(**dbconfig)
cursor = db.cursor()
cursor.execute(query)
rows = cursor.fetchall()



print rows
