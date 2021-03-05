from main import call_method_carpet, call_method_mirror
import psycopg2
import os
import logging

#print(os.environ["scrap_mdp"])
logging.basicConfig(filename = "db_scrapping.log", 
                    level= logging.DEBUG, 
                    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')



class Table():
    
    def __init__(self):

        host = "scrapper-mdm.postgres.database.azure.com"
        dbname = "my_db"
        user = "marwa_admin@scrapper-mdm"
        password = "MaisonduMonde!123"
        sslmode = "require" 

        conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
        #print(conn_string)
        self.conn = psycopg2.connect(conn_string)
        self.cursor = self.conn.cursor()


        self.my_call_carpet = call_method_carpet()
        self.my_call_mirror = call_method_mirror()
    

    def create_table_carpet(self):
        
        logging.info("[POSTGRES] Creation table carpet : start")

        #self.cursor.execute("DROP TABLE carpet")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS carpet (id serial PRIMARY KEY, carpet_name VARCHAR(255) NOT NULL, carpet_description VARCHAR(255) NOT NULL, carpet_dimention VARCHAR(255) NOT NULL, carpet_price VARCHAR(30) NOT NULL, carpet_date VARCHAR(40) NOT NULL)")
        self.conn.commit()
        logging.info("[POSTGRES] Creation table carpet : end")

    def file_carpet_table(self):

        logging.info("[POSTGRES] Insert data in table mirror : start")

        try:
            insert = "INSERT INTO carpet (carpet_name, carpet_description, carpet_dimention, carpet_price, carpet_date) VALUES(%s, %s, %s, %s, %s);"
            value = self.my_call_carpet
            #print('value of carpet table',value)
            self.cursor.executemany(insert, value)

            self.conn.commit()
        except Exception as e:
            logging.error('[POSTGRES] ERROOOOR !! empty list, didnt fill carpet table' +str(e))

        logging.info("[POSTGRES] Insert data in table mirror : end")


    def create_table_mirror(self):

        logging.info("[POSTGRES] Creation table mirror : start")

        
        #self.cursor.execute("DROP TABLE mirror")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS mirror (id serial PRIMARY KEY, mirror_named VARCHAR(255) NOT NULL, mirror_description VARCHAR(255) NOT NULL, mirror_dimention VARCHAR(255) NOT NULL, mirror_price VARCHAR(30) NOT NULL, mirror_date VARCHAR(255))")
        self.conn.commit()

        logging.info("[POSTGRES] Creation table mirror : end")


    
    def file_mirror_table(self):
        #print("hello")
        logging.info("[POSTGRES] Insert data in table mirror : start")

        
        try:
            
            insert = "INSERT INTO mirror (mirror_named, mirror_description, mirror_dimention, mirror_price, mirror_date) VALUES(%s, %s, %s, %s, %s)"
            #print(insert)
            value= self.my_call_mirror
            #print('value of mirror table',value)
            self.cursor.executemany(insert, value)
            self.conn.commit()
        except Exception as e:
            logging.error("[POSTGRES] ERROOOOOOR !!!! list empty, didn't fill mirror db" +str(e))

        logging.info("[POSTGRES] Insert data in table mirror : end")

        try:
            insert_date = "INSERT INTO mirror (mirror_date) VALUES (%s)"
            value_date = my_datetime
            self.cursor.executemany(insert, value)
            self.conn.commit()
        except Exception as e:
            logging.error("[POSTGRES] ERROOOOOOR !!!! datetime wasn't inserted" +str(e))


    def delete_duplicate_carpet(self):

        #self.cursor.execute("SELECT COUNT(*) AS cnt FROM carpet GROUP BY carpet_description, carpet_price, carpet_name HAVING  cnt > 1")
        #self.cursor.execute("DELETE FROM carpet WHERE ctid IN (SELECT ctid FROM (SELECT ctid, ROW_NUMBER() OVER (PARTITION BY carpet_description, carpet_name,carpet_price) AS rn FROM   my_table) t WHERE  rn > 1);")
        self.cursor.execute("DELETE FROM carpet WHERE carpet.ctid NOT IN (SELECT ctid FROM (SELECT DISTINCT ON (carpet_name, carpet_description, carpet_price) * FROM carpet));")
        self.conn.commit()


my_table = Table()

#################################

try:
    my_table.create_table_carpet()
    logging.info("[POSTGRES] Created table carpet with success")
except:
    logging.warning("[POSTGRES] Failed to create carpet table, check conditions, connections or syntaxe")


try:
    my_table.file_carpet_table()
    logging.info("[POSTGRES] Insert within carpet table with success")

except Exception as e:
    logging.warning("[POSTGRES] Failed to insert data in carpet table, check conditions, zipped listn connections or syntaxe" + str(e))

# try:
#     #my_table.delete_duplicate_carpet()
#     logging.info("[POSTGRES] delete duplicate with sucess")
# except Exception as e:
#     logging.info("[POSTGRES] failed to delete duplicate " + str(e))


# # ###############################

try:
    my_table.create_table_mirror()
    logging.info("[POSTGRES] Created table mirror with success")
except:
    logging.warning("[POSTGRES] Failed to create mirror table, check conditions, connections or syntaxe")

try:
    my_table.file_mirror_table()
    logging.info("[POSTGRES] Insert within mirror table with success")
except:
    logging.warning("[POSTGRES] Failed to insert data in mirror table, check conditions, zipped listn connections or syntaxe")

