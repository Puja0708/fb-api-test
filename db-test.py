
import sqlite3

sqlite_file = '/home/puja/Documents/fb-api-test/test.db'    # name of the sqlite database file
table_name1 = 'table_1'	# name of the table to be created
table_name2 = 'table_2'	# name of the table to be created
new_field = 'my_1st_column' # name of the column
field_type = 'INTEGER'  # column data type

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE IF NOT EXISTS table_1 (a integer)')

# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
# c.execute('CREATE TABLE IF NOT EXISTS (aa integer PRIMARY KEY)')

var1 = 6
var2 = "aa"

query = "INSERT INTO table_1 (a) VALUES (?)"
# query1 = "INSERT INTO table_1 VALUES (" + var1 + ")"
# query2 = "INSERT INTO table_2 VALUES (" + var2 + ")"

c.execute("insert into table_1(a) values (?)",(var1,))

conn.commit()