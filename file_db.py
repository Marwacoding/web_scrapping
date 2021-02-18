import mysql.connector
import logging
#import pandas as pd
from main import *


logging.basicConfig(filename = "web_scrapping.log", 
    level= logging.INFO, format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')


class Table_carpet():

    
    def __init__(self):
        self.mydb = mysql.connector.connect (
        host="scrap_sql",
        user="root",
        database = "my_db",
        password="123",
        )

        self.c = self.mydb.cursor()

    #conn = sqlite3.connect("my_db.db")
    #c = conn.cursor()


    def create_table_carpet(self):
        
        #print("hello")

        self.c.execute("DROP TABLE carpet")
        self.c.execute("CREATE TABLE IF NOT EXISTS carpet (id INTEGER AUTO_INCREMENT PRIMARY KEY , carpet_name VARCHAR(255) NOT NULL, carpet_description VARCHAR(255) NOT NULL, carpet_dimention VARCHAR(255) NOT NULL, carpet_price VARCHAR(30) NOT NULL)")



    def file_carpet_table(self):
        #logging.info('Inserting my data from my webscrapping: start')
        #for name, description, dimension, price in zip(my_carpet_name, my_desc, my_dim, prices):
                #print(name) print(description) print(dimension) print(price)
        insert = "INSERT INTO carpet (carpet_name, carpet_description, carpet_dimention, carpet_price) VALUES(%s, %s, %s, %s);"
        value= my_carpets.zip_list()
        #print(value)
        self.c.executemany(insert, value)
                #c.executemany("INSERT INTO carpet (carpet_name, carpet_description, carpet_dimention, carpet_price) VALUES(%s, %s, %s, %s); (name, description, dimension, price)")
        self.mydb.commit()




class Table_mirror():

    def __init__(self):
        self.mydb = mysql.connector.connect (
        host="scrap_sql",
        user="root",
        database = "my_db",
        password="123",
        )

        self.c = self.mydb.cursor()

    def create_table_mirror(self):
        
        #print("hello")

        self.c.execute("DROP TABLE mirror")
        self.c.execute("CREATE TABLE IF NOT EXISTS mirror (id INTEGER AUTO_INCREMENT PRIMARY KEY , mirror_named VARCHAR(255) NOT NULL, mirror_description VARCHAR(255) NOT NULL, mirror_dimention VARCHAR(255) NOT NULL, mirror_price VARCHAR(30) NOT NULL)")


    
    def file_mirror_table(self):
        #logging.info('Inserting my data from my webscrapping: start')
        #for name, description, dimension, price in zip(my_carpet_name, my_desc, my_dim, prices):
                #print(name) print(description) print(dimension) print(price)
        insert = """INSERT INTO mirror (mirror_named, mirror_description, mirror_dimention, mirror_price) VALUES(%s, %s, %s, %s)"""
        value= my_mirror.zip_list_mirror()
        #print(value)
        self.c.executemany(insert, value)
                #c.executemany("INSERT INTO carpet (carpet_name, carpet_description, carpet_dimention, carpet_price) VALUES(%s, %s, %s, %s); (name, description, dimension, price)")
        self.mydb.commit()




my_carpet_table = Table_carpet()
create_my_carpet_table = my_carpet_table.create_table_carpet()
#print(create_my_carpet_table)
insert_to_carpet_table = my_carpet_table.file_carpet_table()
#print(insert_to_carpet_table)


my_mirror_table = Table_mirror()
create_my_mirror_table = my_mirror_table.create_table_mirror()
insert_to_mirror_table = my_mirror_table.file_mirror_table()

