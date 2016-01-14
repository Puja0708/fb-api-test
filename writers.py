from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

DEBUG = True
database_location = '/var/lib/mysql/sportskeeda'
table_name = 'keeda_author_fact'

query = 'select author_id, author_url, author_title, author_post_count, total_reads, author_rss from keeda_author_fact ORDER BY author_post_count'
dbconfig = read_db_config()
conn = MySQLConnection(**dbconfig)
cursor = conn.cursor()
cursor.execute(query)
rows = cursor.fetchall()

print rows
