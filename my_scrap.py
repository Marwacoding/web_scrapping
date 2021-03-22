#!/usr/bin/python

import re
import requests
import datetime
from bs4 import BeautifulSoup #pour utiliser BeautifulSoup j'ai besoin de bs4
import logging
import unidecode
# https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#https://stackoverflow.com/questions/27981545/suppress-insecurerequestwarning-unverified-https-request-is-being-made-in-pytho

logging.basicConfig(filename = "web_scrapping.log", level= logging.DEBUG, 
                    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')
#print('hello main')

class Mycarpet() :



    def __init__(self):
        
        try:
            self.response = requests.get('https://www.maisonsdumonde.com/FR/fr/c/tapis-1559ac122904996dcae8be4c5de8fda6', verify=False, timeout=5)
        except Exception as e :
        #https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
            logging.error("[SCRAP] failed to access url, check connection or url" + str(e))


        self.maison_du_monde = self.response.text 
        self.data = BeautifulSoup(self.maison_du_monde,"html.parser")

        self.final_item = []
        self.names = []
        self.desc = []
        self.dim = []
        self.final_price = []
        self.result_carpet = []
        self.carpet_date = []
    
    #print("working ?")
        
    def carpet(self):
        logging.info("[SCRAP] accessing carpet info -- Start")
        
        title_item = self.data.find_all("h2", class_= "font-weight-normal expand-link name mb-0")
        carpet_list = []

        try:
            for k, item in enumerate(title_item):
                title = item.getText()
                #print('this is all my html carpet element',title)
                carpet_list.append(title)
                self.final_item.append(carpet_list[k])
            #enumerate and k index to stop the iteration once all the items are filled in list
            #print(self.final_item)
            #return self.final_item
        except Exception as e:
            logging.error("[SCRAP] ERROR!!!!!! Carpet info's list may be out of range" +str(e))
        
        logging.info("[SCRAP] accessing carpet info -- End")

        

    def carpet_name(self):
        logging.info("[SCRAP] accessing carpet name -- Start")

        try:
            for i in self.final_item:
                #print('all my items',i)
                if len(i.split(" - "))==2:
                    self.names.append(i.split(" - ")[0])
                #print('name of carptet ',self.names)

            logging.info("[SCRAP] accessing carpet name -- End")

            return self.names
        except Exception as e :
            logging.error("[SCRAP] ERROR !!!!!!!! Carpet name's list is not created, check the conditions" + str(e))


        logging.info("[SCRAP] accessing carpet name -- End")
        


    def carpet_desc(self):
        logging.info("[SCRAP] accessing carpet descripsion -- Start")

        try:
            for i in self.final_item:
                if len(i.split(" - "))==2:
                    unaccented_string = unidecode.unidecode(i)
                    
                    try:
                        description_sublist = re.split("(?<=\D)(?=\d)", unaccented_string.split(" - ")[1], maxsplit=1)
                        desc_item = [[item] for items in description_sublist for item in items.split(",")][0][0]
                        self.desc.append(desc_item)
                    except Exception as e:
                        logging.error("split method in carpet descripsion is expecting a bytes-like object" +str(e))

            logging.info("[SCRAP] accessing carpet descripsion -- End")

            return self.desc

        except Exception as e:
            logging.warning("[SCRAP] Carpet descripsion's list is not created, check the conditions" +str(e))


        



    def carpet_dim(self):
        logging.info("[SCRAP] accessing carpet dimention -- Start")

        try:
            for i in self.final_item:
                if len(i.split(" - "))==2:
                    try:
                        dim_item =re.split("(?<=\D)(?=\d)", i, maxsplit= 1)[1]
                        self.dim.append(dim_item)
                    except Exception as e:
                        logging.error("[SCRAP] ERROOOOOR !!!!! Carpet dimension list may be out of range, print %s to check the content %s" %(i, str(e)))

            logging.info("[SCRAP] accessing carpet dimention -- End")

            return self.dim

        except Exception as e:
            logging.warning("[SCRAP] Carpet dimension's list is not created, it may have an NameError or a SyntaxError." + str(e))

    def carpet_dates(self):
        logging.info("[SCRAP] accessing carpet dates -- Start")

        try:
            for i in self.final_item:
    
                my_datetime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                self.carpet_date.append(my_datetime)
            

            logging.info("[SCRAP] accessing mirror date -- End")

            return self.carpet_date



        except Exception as e:
            logging.warning("[SCRAP] Carpet date list is not created" + str(e))

        


    def carpet_price(self):
        logging.info("[SCRAP] accessing carpet price -- Start")

        item_price = self.data.find_all("div", class_= "ml-auto font-weight-semibold price")
        #print(item_price)

        item_list = []
        try:
            for k, item in enumerate(item_price):
                price = item.getText()
                item_list.append(price)
                #final_price.append(item_list[k])
                self.final_price.append(item_list[k].split()[0])

            logging.info("[SCRAP] accessing carpet price -- End")

            return self.final_price

        except Exception as e:
            logging.error("[SCRAP] Carpet price list is not created, check the conditions" + str(e))

        logging.info("[SCRAP] accessing carpet price -- End")


    def zip_carpet_list(self): 
        logging.info("[SCRAP] ziping all list to tranfer db-- Start")

        #print("this is carpet name",self.names)
        #print("this is carpet desc",self.desc)
        #print("this is carpet dim",self.dim)
        #print("this is carpet price",self.final_price)
        #print(self.names, self.desc, self.dim, self.final_price)
        try:
            self.result_carpet = list(zip(self.names, self.desc, self.dim, self.final_price, self.carpet_date))
            #print("this zip carpet in web_scrap", self.result_carpet)
        except Exception as e:
            logging.error("[SCRAP] ERROR !!! zip list of carpet is not created, check the conditions will affect mysql table" + str(e))

        logging.info("[SCRAP] ziping all list to tranfer db-- End")

        return self.result_carpet

        


        
class Mirror(): 

    def __init__(self): 

        logging.info('Accessing mirror class: start')

        try:
            self.response_mirror = requests.get('https://www.maisonsdumonde.com/FR/fr/c/miroirs-484554f26aa42ef448cafd6fe7ad385e', timeout=5, verify=False)
        except Exception as e:
            logging.error("[SCRAP] failed to access url, check connection or url" + str(e))

        self.maison_du_monde_mirror = self.response_mirror.text 
        self.data = BeautifulSoup(self.maison_du_monde_mirror,"html.parser")
        
        self.mirror_name_list = []
        self.mirror_names = []
        self.mirror_desc = []
        self.mirror_dim = []
        self.mirror_price_list = []
        self.final_mirror = []
        self.result_mirror = []
        self.mirror_date = []

        logging.info('[SCRAP] Accessing mirror class: end')

    
    def name_mirror_total(self):
        
        logging.info('[SCRAP] Accessing mirros name: start')

        mirror_name = []
        title_name = self.data.find_all("h2", class_= "font-weight-normal expand-link name mb-0")

        try:
            for k, item in enumerate(title_name):
                title = item.getText()
                mirror_name.append(title)
                self.mirror_name_list.append(mirror_name[k])
                #print(mirror_name_list)
            return self.mirror_name_list

            logging.info('Accessing mirrors name: End')

        except Exception as e:
            logging.error("[SCRAP] ERROOOOR !!! mirror info's list may be out of range" + str(e))

        


    def mirror_name(self):

        logging.info("[SCRAP] accessing mirror name -- Start")

        try:
            for i in self.mirror_name_list:
                #print(i)
                if len(i.split(" - "))==2:

                    unaccented_string = unidecode.unidecode(i)

                    self.mirror_names.append(unaccented_string.split(" - ")[0])

            logging.info("[SCRAP] accessing mirror name -- End")

            return self.mirror_names

        except Exception as e:
            logging.error("[SCRAP] Erroooooor !!! Mirror name's list is not created, check the conditions" + str(e))

        logging.info("accessing mirror name -- End")


    def mirror_description(self):
        logging.info("[SCRAP] accessing mirror description -- Start")

        try:
            for i in self.mirror_name_list:
                if len(i.split(" - "))==2:
                    unaccented_string = unidecode.unidecode(i)
                    try:
                        description_sublist = re.split("(?<=\D)(?=\d)", unaccented_string.split(" - ")[1], maxsplit=1)
                        desc_item = [[item] for items in description_sublist for item in items.split(",")][0][0]
                        self.mirror_desc.append(desc_item)
                    except Exception as e:
                        logging.error("[SCRAP] ERROR !!! Mirror descripsion list may be out of range, print %s to check the content %s" %(i, str(e)))

            logging.info("[SCRAP] accessing mirror description -- End")


            return self.mirror_desc

        except Exception as e:
            logging.error("[SCRAP] ERROR !!!!!! Mirror descripsion's list is not created, check the conditions" +str(e))


        

    def mirror_dimension(self):
        logging.info("[SCRAP] accessing mirror dimension -- Start")

        try:

            for i in self.mirror_name_list:

                try:
                    if len(i.split(" - "))==2:
                        dim_item =re.split("(?<=\D)(?=\d)", i, maxsplit= 1)[1]
                        self.mirror_dim.append(dim_item)
                except Exception as e:
                    logging.error('[SCRAP] ERROORR !!! Mirror dimension list may be out of range, print %s to check the content %s' %(i, str(e)))

            logging.info("[SCRAP] accessing mirror dimension -- End")

            return self.mirror_dim

            

        except Exception as e:
            logging.warning("[SCRAP] ERROOOOR !!! Mirror dimension's list is not created, it may have an NameError or a SyntaxError." +str(e))



    def mirror_dates(self):
        logging.info("[SCRAP] accessing mirror date -- Start")

        try:

            for i in self.mirror_name_list:

                my_datetime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                self.mirror_date.append(my_datetime)
            

            logging.info("[SCRAP] accessing mirror date -- End")

            return self.mirror_date

        except Exception as e:
            logging.warning("[SCRAP] ERROOOOR !!! Mirror date has issue ==> " +str(e))


    def price_mirror(self):

        logging.info('[SCRAP] Getting my mirror price: start')

        mirror_price = []
        price_text = self.data.find_all("div", class_="ml-auto font-weight-semibold price")
        try:
            for k, item in enumerate(price_text): 
                price = item.getText()
                mirror_price.append(price)
                self.mirror_price_list.append(mirror_price[k].split()[0])
            return self.mirror_price_list

            logging.info('[SCRAP] Getting my mirror price: End')

        except Exception as e:
            logging.error("[SCRAP] Mirror price list is not created, check the conditions" + str(e))





    def zip_list_mirror(self):

        logging.info('[SCRAP] Zipping all my lists in tuple: start')
        
        try:
            #print("this is mirror names", self.mirror_price_list)
            self.result_mirror= zip(self.mirror_names, self.mirror_desc, self.mirror_dim, self.mirror_price_list, self.mirror_date)
            #print('this is zip mirror',self.result_mirror)

            logging.info('[SCRAP] Zipping all my lists in tuple: End')

            return self.result_mirror
            
        except Exception as e:
            logging.error("[SCRAP] ERROR !!! zip list of mirror is not created " +str(e))


        

