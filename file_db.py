import mysql.connector
#import pandas as pd
from main import *


mydb = mysql.connector.connect(
  host="scrap_sql",
  user="root",
  password="123",
  auth_plugin='mysql_native_password'
  )


c = mydb.cursor()

#conn = sqlite3.connect("my_db.db")
#c = conn.cursor()


# def create_db():
    
#     print("hello")

# # Create the table, read the article below if you
# # are unsure of what they mean
# # https://www.w3schools.com/sql/sql_datatypes.asp

#     # my_table = """ CREATE TABLE carpet (
#     #                 id INTEGER PRIMARY KEY NOT NULL,
#     #                 carpet_name VARCHAR(100),
#     #                 price VARCHAR(30),
#     #                 )"""

#     c.execute("DROP TABLE carpet")
#     c.execute("CREATE TABLE IF NOT EXISTS carpet (id INTEGER PRIMARY KEY , carpet_name VARCHAR(255) NOT NULL, carpet_description VARCHAR(255) NOT NULL, carpet_dimention VARCHAR(255) NOT NULL, price VARCHAR(30) NOT NULL)")
#     #c.execute("INSERT INTO carpet Values(1,'Nom','prix')")
#     #c.execute("SELECT * FROM carpet")
#     #conn.commit()

#     # Remember to save + close



# create_db()



# def read_from_db():

#     for name, description, dimension, price in zip(my_carpet_name, my_desc, my_dim, prices):
#             #print(i)
#             #print(j)
#             c.execute("INSERT INTO carpet (carpet_name, carpet_description, carpet_dimention, price) VALUES(?, ?, ?, ?) ;", (name, description, dimension, price))
#     #conn.commit()

#     c.execute("SELECT * FROM carpet")
#     #conn.commit()

#     for row in c.fetchall():
#         print(row)

#         # df = pd.DataFrame(row)
#         # print(df)
#     #conn.commit()

# read_from_db()