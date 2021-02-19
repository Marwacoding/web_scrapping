import mysql.connector
import logging
#import pandas as pd
from main import *

#print('my db')

logging.basicConfig(filename = "db_scrapping.log", 
    level= logging.INFO, format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')



class Table_carpet():

    def __init__(self):

        logging.info('Connection with sql docker for carpet table: start')

        try:
            self.mydb = mysql.connector.connect (
            host="scrap_sql",
            user="root",
            database = "my_db",
            password="123",
            )
        except(mysql.connector.errors.InterfaceError, mysql.connector.errors.ProgrammingError):
            logging.warning('Failed to connect to docker container, check password, or docker connection')

        try:
            self.c = self.mydb.cursor()
        except AttributeError:
            logging.warning('Failed to establish query, check syntax, will affect creation of table')

        logging.info('Connection with sql connector : end')

    

    def create_table_carpet(self):
        

        self.c.execute("DROP TABLE carpet")
        self.c.execute("CREATE TABLE IF NOT EXISTS carpet (id INTEGER AUTO_INCREMENT PRIMARY KEY , carpet_name VARCHAR(255) NOT NULL, carpet_description VARCHAR(255) NOT NULL, carpet_dimention VARCHAR(255) NOT NULL, carpet_price VARCHAR(30) NOT NULL)")


    def file_carpet_table(self):

        insert = "INSERT INTO carpet (carpet_name, carpet_description, carpet_dimention, carpet_price) VALUES(%s, %s, %s, %s);"
        value= my_carpets.zip_list()

        self.c.executemany(insert, value)

        self.mydb.commit()



class Table_mirror():

    def __init__(self):

        logging.info('Connection with sql docker for mirror table : start')

        try:
            self.mydb = mysql.connector.connect (
            host="scrap_sql",
            user="root",
            database = "my_db",
            password="123",
            )
        except(mysql.connector.errors.InterfaceError, mysql.connector.errors.ProgrammingError):
            logging.warning('Failed to connect to docker container, check password, or docker connection')

        try:
            self.c = self.mydb.cursor()
        except AttributeError:  
            logging.warning('Failed to establish query, check syntax, will affect creation of table')

        logging.info('Connection with sql docker for mirror table : start')



    def create_table_mirror(self):
        
        self.c.execute("DROP TABLE mirror")
        self.c.execute("CREATE TABLE IF NOT EXISTS mirror (id INTEGER AUTO_INCREMENT PRIMARY KEY , mirror_named VARCHAR(255) NOT NULL, mirror_description VARCHAR(255) NOT NULL, mirror_dimention VARCHAR(255) NOT NULL, mirror_price VARCHAR(30) NOT NULL)")


    
    def file_mirror_table(self):
        insert = "INSERT INTO mirror (mirror_named, mirror_description, mirror_dimention, mirror_price) VALUES(%s, %s, %s, %s)"
        value= my_mirror.zip_list_mirror()
        self.c.executemany(insert, value)
        self.mydb.commit()


