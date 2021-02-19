from my_scrap import *
from file_db import *
#from file_db import *

#print("hello")

logging.basicConfig(level=logging.DEBUG,
                    filename="main_scrap.log",
                    filemode="a", #append ou W pour écraser
                    format='%(asctime)s : %(levelname)s : %(message)s')




def main(): 

    
    my_carpets = Mycarpet()

    try:
        item= my_carpets.carpet()
        logging.info("Scrapping carpet items with success")

    except:
        logging.warning("Failed to access carpet items from scrapping, check condition")


    try:
        my_name = my_carpets.carpet_name()
        #print(my_name)
        logging.info("Accessing carpet names with success")

    except:
        logging.warning("Failed to access carpet name, check condition")


    try:
        my_desc = my_carpets.carpet_desc()
        #print(my_desc)
        logging.info("Accessing carpet descripsion with success")
    except:
        logging.warning("Failed to access carpet descripsion, check condition")


    try:
        my_dim = my_carpets.carpet_dim()
        #print(my_dim)
        logging.info("Accessing carpet dimension with success")
    except:
        logging.warning("Failed to access carpet dimension, check condition")


    try:
        prices = my_carpets.carpet_price()
        #print(prices)
        logging.info("Accessing carpet prices with success")
    except:
        logging.warning("Failed to access carpet prices, check condition")


    try:
        results = my_carpets.zip_list()
        #print(results)
        logging.info("Ziping all my carpet info list with success")
    except:
        logging.warning("Failed to zip all list of carpet list, check each one of them to resolve the issue")


    #####################################################


    my_mirror = Mirror()

    try:
        mirror_total = my_mirror.name_mirror_total()
        #print(mirror_total)
        logging.info("Scrapping mirror items with success")
    except:
        logging.warning("Failed to access mirror items from scrapping, check condition")


    try:
        mirror_name = my_mirror.mirror_name()
        #print(mirror_name)
        logging.info("Accessing mirror names with success")
    except:
        logging.warning("Failed to access mirror name, check condition")


    try:
        mirror_desc = my_mirror.mirror_description()
        #print(mirror_desc)
        logging.info("Accessing mirror descripsion with success")
    except:
        logging.warning("Failed to access mirror descripsion, check condition")

    try:
        mirror_dim = my_mirror.mirror_dimention()
        #print(mirror_dim)
        logging.info("Accessing mirror dimention with success")
    except:
        logging.warning("Failed to access mirror dim, check condition")

    try:
        mirror_price = my_mirror.price_mirror()
        #print(mirror_price)
        logging.info("Accessing mirror prices with success")
    except:
        logging.warning("Failed to access prices, check condition")

    try:
        mirror_zip = my_mirror.zip_list_mirror()
        #print(mirror_zip)
        logging.info("Ziping all my mirror info list with success")
    except:
        logging.warning("Failed to zip all list of mirror list, check each one of them to resolve the issue")

   
    #####################################################


    my_table = Table_carpet()

    try:
        create_my_db = my_table.create_table_carpet()
        logging.info("Created table carpet with success")
    except:
        logging.warning("Failed to create carpet table, check conditions, connections or syntaxe")


    try:
        insert_to_db = my_table.file_carpet_table()
        logging.info("Insert within carpet table with success")
   
    except:
        logging.warning("Failed to insert data in carpet table, check conditions, zipped listn connections or syntaxe")


    #######################################################


    my_mirror_table = Table_mirror()

    try:
        create_my_mirror_table = my_mirror_table.create_table_mirror()
        logging.info("Created table mirror with success")
    except:
        logging.warning("Failed to create mirror table, check conditions, connections or syntaxe")

    try:
        insert_to_mirror_table = my_mirror_table.file_mirror_table()
        logging.info("Insert within mirror table with success")
    except:
        logging.warning("Failed to insert data in mirror table, check conditions, zipped listn connections or syntaxe")




if __name__ == '__main__':
    main()

