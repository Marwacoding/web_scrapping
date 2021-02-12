
import sqlite3
from main import *

conn = sqlite3.connect("my_db.db")
c = conn.cursor()


def create_db():
    
    print("hello")

# Create the table, read the article below if you
# are unsure of what they mean
# https://www.w3schools.com/sql/sql_datatypes.asp

    # my_table = """ CREATE TABLE carpet (
    #                 id INTEGER PRIMARY KEY NOT NULL,
    #                 carpet_name VARCHAR(100),
    #                 price VARCHAR(30),
    #                 )"""

    c.execute("DROP TABLE carpet")
    c.execute("CREATE TABLE IF NOT EXISTS carpet ( id INTEGER PRIMARY KEY NOT NULL, carpet_name VARCHAR(100),price VARCHAR(30))")
    c.execute("INSERT INTO carpet Values(1,'Nom','prix')")
    c.execute("SELECT * FROM carpet")
    conn.commit()

    # Remember to save + close



create_db()

def read_from_db():
    c.execute ('SELECT * FROM carpet ') 
for row in c.fetchall():
    print(row)

read_from_db()


##
#query = pragma table_info('db_table')
#query show databases; =  "PRAGMA database_list;"
'''
 # Insert some users into our database
 def insert_db():
 conn = sqlite3.connect("database.db")
 c = conn.cursor()
 c.execute(
 """INSERT INTO emp VALUES (23, "Rishabh", "Bansal",
 "M", "2014-03-28");""")
 c.execute(
 """INSERT INTO emp VALUES (1, "Bill", "Gates", "M",
 "1980-10-28");""")
 # Remember to save + close
 conn.commit()
 conn.close()
 # Fetch the data
 def select_from_db():
 conn = sqlite3.connect("database.db")
 c = conn.cursor()
c.execute("SELECT * FROM emp")
 # Store + print the fetched data
 result = c.fetchall()
 for i in result:
 print(i)
 # Remember to save + close
 conn.commit()
 '''