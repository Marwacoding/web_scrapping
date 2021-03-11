import mysql.connector
import logging
from my_scrap import *
from postgres import *
from main import call_method_carpet, call_method_mirror


#print('my db')
#my_carpets = Mycarpet()
#print('test', my_carpets)

logging.basicConfig(filename = "db_scrapping.log", 
                    level= logging.DEBUG, 
                    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')



class Table():

    def __init__(self):

        logging.info('[SQL] Connection with sql docker for carpet table: start')

        try:
            self.mydb = mysql.connector.connect (
            host = os.environ["host_sql"],
            database = os.envrion["db_sql"],
            user = os.environ["user_sql"],
            password = os.environ["pw_sql"],
            )
        except(mysql.connector.errors.InterfaceError, mysql.connector.errors.ProgrammingError):
            logging.warning('[SQL] Failed to connect to docker container, check password, or docker connection')

        try:
            self.c = self.mydb.cursor()
        except AttributeError:
            logging.warning('[SQL] Failed to establish query, check syntax, will affect creation of table')

        logging.info('[SQL] Connection with sql connector : end')

        self.my_call_carpet = call_method_carpet()
        self.my_call_mirror = call_method_mirror()
    

    def create_table_carpet(self):
        
        logging.info("[SQL] Creation table carpet : start")

        self.c.execute("DROP TABLE carpet")
        self.c.execute("CREATE TABLE IF NOT EXISTS carpet (id INTEGER AUTO_INCREMENT PRIMARY KEY , carpet_name VARCHAR(255) NOT NULL, carpet_description VARCHAR(255) NOT NULL, carpet_dimention VARCHAR(255) NOT NULL, carpet_price VARCHAR(30) NOT NULL, carpet_date VARCHAR(40) NOT NULL)")

        logging.info("[SQL] Creation table carpet : end")

    def file_carpet_table(self):

        logging.info("[SQL] Insert data in table mirror : start")

        try:
            insert = "INSERT INTO carpet (carpet_name, carpet_description, carpet_dimention, carpet_price, carpet_date) VALUES(%s, %s, %s, %s, %s);"
            value = self.my_call_carpet
            #print('value of carpet table',value)
            self.c.executemany(insert, value)

            self.mydb.commit()
        except Exception as e:
            logging.error('[SQL] ERROOOOR !! empty list, didnt fill carpet table' +str(e))

        logging.info("[SQL] Insert data in table mirror : end")


    def create_table_mirror(self):

        logging.info("[SQL] Creation table mirror : start")

        
        self.c.execute("DROP TABLE mirror")
        self.c.execute("CREATE TABLE IF NOT EXISTS mirror (id INTEGER AUTO_INCREMENT PRIMARY KEY , mirror_named VARCHAR(255) NOT NULL, mirror_description VARCHAR(255) NOT NULL, mirror_dimention VARCHAR(255) NOT NULL, mirror_price VARCHAR(30) NOT NULL, mirror_date VARCHAR(255))")

        ogging.info("[SQL] Creation table mirror : end")


    
    def file_mirror_table(self):
        #print("hello")
        logging.info("[SQL] Insert data in table mirror : start")

        
        try:
            
            insert = "INSERT INTO mirror (mirror_named, mirror_description, mirror_dimention, mirror_price, mirror_date) VALUES(%s, %s, %s, %s, %s)"
            #print(insert)
            value= self.my_call_mirror
            #print('value of mirror table',value)
            self.c.executemany(insert, value)
            self.mydb.commit()
        except Exception as e:
            logging.error("[SQL] ERROOOOOOR !!!! list empty, didn't fill mirror db" +str(e))

        logging.info("[SQL] Insert data in table mirror : end")

        try:
            insert_date = "INSERT INTO mirror (mirror_date) VALUES (%s)"
            value_date = my_datetime
            self.c.executemany(insert, value)
            self.mydb.commit()
        except Exception as e:
            logging.error("[SQL] ERROOOOOOR !!!! datetime wasn't inserted" +str(e))





my_table = Table()

#################################

try:
    my_table.create_table_carpet()
    logging.info("[SQL] Created table carpet with success")
except:
    logging.warning("[SQL] Failed to create carpet table, check conditions, connections or syntaxe")


try:
    my_table.file_carpet_table()
    logging.info("[SQL] Insert within carpet table with success")

except Exception as e:
    logging.warning("[SQL] Failed to insert data in carpet table, check conditions, zipped listn connections or syntaxe" + str(e))


# ###############################

try:

    my_table.create_table_mirror()
    logging.info("[SQL] Created table mirror with success")
except:
    logging.warning("[SQL] Failed to create mirror table, check conditions, connections or syntaxe")

try:
    my_table.file_mirror_table()
    logging.info("[SQL] Insert within mirror table with success")
except:
    logging.warning("[SQL] Failed to insert data in mirror table, check conditions, zipped listn connections or syntaxe")


# def reset_logfile(logfile_path):
#             ### Reset du fichier log
#         my_txt_file= open(logfile_path, "r+")    
#         # to erase all data  
#         my_txt_file.truncate() 
#         # to close file
#         my_txt_file.close()

# reset_logfile("web_scrapping.log")