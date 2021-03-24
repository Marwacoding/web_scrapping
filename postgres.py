from main import *
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
import logging

#print(os.environ["pw"])
logging.basicConfig(filename = "db_scrapping.log", 
                    level= logging.DEBUG, 
                    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')



host = os.environ["host"]
dbname = os.environ["db"]
#user = os.environ["user"]
#password = os.environ["pw"]
#sslmode = "require" 

conn_string = "host={0} dbname={1}".format(host, dbname)
conn = psycopg2.connect(conn_string)

cursor = conn.cursor()
 

def erase_table():
    cursor.execute("DROP Table Carpet")
    cursor.execute("DROP Table Mirror")
    conn.commit()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS carpet (ID SERIAL PRIMARY KEY , NOM VARCHAR(255), PRIX VARCHAR(30))")
    cursor.execute("CREATE TABLE IF NOT EXISTS mirror (ID SERIAL PRIMARY KEY, NOM VARCHAR(255), PRIX VARCHAR(30))")
    conn.commit()

def insert_info():
    carpet_sql = "INSERT INTO carpet (NOM, PRIX) VALUES (%s,%s)"
    carpet_valeur = c.zip_list_carpet()
    cursor.executemany(carpet_sql, carpet_valeur)
    
    mirror_sql = "INSERT INTO mirror (NOM, PRIX) VALUES (%s,%s)"
    mirror_valeur = m.zip_list_mirror()
    cursor.executemany(mirror_sql, mirror_valeur)

    conn.commit()

    erase_table()
    create_table()
    insert_info()

    cursor.close()
    conn.close()


 