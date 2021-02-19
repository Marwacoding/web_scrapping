import re
import requests
from bs4 import BeautifulSoup #pour utiliser BeautifulSoup j'ai besoin de bs4
import logging
import unidecode
# https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#https://stackoverflow.com/questions/27981545/suppress-insecurerequestwarning-unverified-https-request-is-being-made-in-pytho




class Mycarpet() :

    logging.basicConfig(filename = "web_scrapping.log", 
    level= logging.DEBUG, format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')


    def __init__(self):
        
        try:
            self.response = requests.get('https://www.maisonsdumonde.com/FR/fr/c/tapis-1559ac122904996dcae8be4c5de8fda6', verify=False, timeout=5)
        except (requests.exceptions.ConnectionError, requests.ConnectionError) :
        #https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
            logging.warning("failed to access url, check connection or url")


        self.maison_du_monde = self.response.text 
        self.data = BeautifulSoup(self.maison_du_monde,"html.parser")

        self.final_item = []
        self.names = []
        self.desc = []
        self.dim = []
        self.final_price = []
        self.result = []
        
        
    def carpet(self):
        logging.info("accessing carpet info -- Start")
        
        title_item = self.data.find_all("h2", class_= "font-weight-normal expand-link name mb-0")
        carpet_list = []

        try:
            for k, item in enumerate(title_item):
                title = item.getText()
                carpet_list.append(title)
                self.final_item.append(carpet_list[k])
        except (IndexError, TypeError):
            logging.warning("Carpet info's list may be out of range")
        
        logging.info("accessing carpet info -- End")

        

    def carpet_name(self):
        logging.info("accessing carpet name -- Start")

        try:
            for i in self.final_item:
                #print(i)
                if len(i.split(" - "))==2:
                    self.names.append(i.split(" - ")[0])
                #print('name of carptet  1= ',self.names)
                else:
                    logging.warning(f'Carpet name list may be out of range, print {i} to check the content')


            return self.names
        except (IndexError, TypeError, NameError, SyntaxError):
            logging.warning("Carpet name's list is not created, check the conditions")


        logging.info("accessing carpet name -- End")
        


    def carpet_desc(self):
        logging.info("accessing carpet descripsion -- Start")

        try:
            for i in self.final_item:
                if len(i.split(" - "))==2:
                    unaccented_string = unidecode.unidecode(i)
                    
                    try:
                        description_sublist = re.split("(?<=\D)(?=\d)", unaccented_string.split(" - ")[1], maxsplit=1)
                        desc_item = [[item] for items in description_sublist for item in items.split(",")][0][0]
                    except TypeError:
                        logging.warning("split method in carpet descripsion is expecting a bytes-like object")
                    except IndexError:
                        logging.warning(f'Carpet descripsion list may be out of range, print {i} to check the content')

                    self.desc.append(desc_item)

            return self.desc
        except(IndexError, TypeError, NameError, SyntaxError):
            logging.warning("Carpet descripsion's list is not created, check the conditions")


        logging.info("accessing carpet descripsion -- End")



    def carpet_dim(self):
        logging.info("accessing carpet dimention -- Start")

        try:
            for i in self.final_item:
                if len(i.split(" - "))==2:
                    try:
                        dim_item =re.split("(?<=\D)(?=\d)", i, maxsplit= 1)[1]
                        self.dim.append(dim_item)
                    except IndexError:
                        logging.warning(f'Carpet dimension list may be out of range, print {i} to check the content')

        
            return self.dim

        except (IndexError, TypeError, NameError, SyntaxError):
            logging.warning("Carpet dimension's list is not created, it may have an NameError or a SyntaxError.")


        logging.info("accessing carpet dimention -- End")


    def carpet_price(self):
        logging.info("accessing carpet price -- Start")

        item_price = self.data.find_all("div", class_= "ml-auto font-weight-semibold price")
        #print(item_price)

        item_list = []
        try:
            for k, item in enumerate(item_price):
                price = item.getText()
                item_list.append(price)
                #final_price.append(item_list[k])
                self.final_price.append(item_list[k].split()[0])
            return self.final_price
        except (IndexError, TypeError, NameError, SyntaxError):
            logging.warning("Carpet price list is not created, check the conditions")

        logging.info("accessing carpet price -- End")


    def zip_list(self): 
        logging.info("ziping all list to tranfer db-- Start")

        #print("this is name",self.names)
        #print("this is desc",self.desc)
        #print("this is dim",self.dim)
        #print("this is price",self.final_price)
        #print(self.names, self.desc, self.dim, self.final_price)
        try:
            result = list(zip(self.names, self.desc, self.dim, self.final_price))
        except (IndexError, TypeError):
            logging.warning("zip list of carpet is not created, check the conditions will affect mysql table")

        #self.result.append(r)
        
        return result

        logging.info("ziping all list to tranfer db-- End")

        
class Mirror(): 
    def __init__(self): 

        logging.info('Accessing mirror class: start')

        try:
            self.response_mirror = requests.get('https://www.maisonsdumonde.com/FR/fr/c/miroirs-484554f26aa42ef448cafd6fe7ad385e', timeout=5, verify=False)
        except (requests.exceptions.ConnectionError, requests.ConnectionError) :
            logging.warning("failed to access url, check connection or url")

        self.maison_du_monde_mirror = self.response_mirror.text 
        self.data = BeautifulSoup(self.maison_du_monde_mirror,"html.parser")
        
        self.mirror_name_list = []
        self.mirror_names = []
        self.mirror_desc = []
        self.mirror_dim = []
        self.mirror_price_list = []
        self.final_mirror = []

        logging.info('Accessing mirror class: end')


    def name_mirror_total(self):

        logging.info('Accessing mirros name: start')

        mirror_name = []
        title_name = self.data.find_all("h2", class_= "font-weight-normal expand-link name mb-0")

        try:
            for k, item in enumerate(title_name):
                title = item.getText()
                mirror_name.append(title)
                self.mirror_name_list.append(mirror_name[k])
            return self.mirror_name_list
        except (IndexError, TypeError):
            logging.warning("mirror info's list may be out of range")

        logging.info('Accessing mirrors name: End')

    

    def mirror_name(self):

        logging.info("accessing mirror name -- Start")

        try:
            for i in self.mirror_name_list:
                #print(i)
                if len(i.split(" - "))==2:

                    unaccented_string = unidecode.unidecode(i)

                    self.mirror_names.append(unaccented_string.split(" - ")[0])
            return self.mirror_names
        except (IndexError, TypeError, NameError, SyntaxError):
            logging.warning("Mirror name's list is not created, check the conditions")

        logging.info("accessing mirror name -- End")



    def mirror_description(self):
        logging.info("accessing mirror description -- Start")

        try:
            for i in self.mirror_name_list:
                if len(i.split(" - "))==2:
                    unaccented_string = unidecode.unidecode(i)
                    try:
                        description_sublist = re.split("(?<=\D)(?=\d)", unaccented_string.split(" - ")[1], maxsplit=1)
                        desc_item = [[item] for items in description_sublist for item in items.split(",")][0][0]
                    except TypeError:
                        logging.warning("split method in mirror descripsion is expecting a bytes-like object")
                    except IndexError:
                        logging.warning(f'Mirror descripsion list may be out of range, print {i} to check the content')

                    self.mirror_desc.append(desc_item)

            return self.desc

        except(IndexError, TypeError, NameError, SyntaxError):
            logging.warning("Mirror descripsion's list is not created, check the conditions")


        logging.info("accessing mirror description -- End")
    


    def mirror_dimention(self):
        logging.info("accessing mirror dimension -- Start")

        try:
            for i in self.mirror_name_list:

                try:
                    if len(i.split(" - "))==2:
                        dim_item =re.split("(?<=\D)(?=\d)", i, maxsplit= 1)[1]
                        self.mirror_dim.append(dim_item)
                except IndexError:
                    logging.warning(f'Mirror dimension list may be out of range, print {i} to check the content')

            return self.mirror_dim


        except (IndexError, TypeError, NameError, SyntaxError):
            logging.warning("Mirror dimension's list is not created, it may have an NameError or a SyntaxError.")

        logging.info("accessing mirror dimension -- End")



    def price_mirror(self):

        logging.info('Getting my mirror price: start')

        mirror_price = []
        price_text = self.data.find_all("div", class_="ml-auto font-weight-semibold price")
        try:
            for k, item in enumerate(price_text): 
                price = item.getText()
                mirror_price.append(price)
                self.mirror_price_list.append(mirror_price[k].split()[0])
            return self.mirror_price_list
        except (IndexError, TypeError, NameError, SyntaxError):
            logging.warning("Mirror price list is not created, check the conditions")


        logging.info('Getting my mirror price: End')

    

    def zip_list_mirror(self):

        logging.info('Zipping all my lists in tuple: start')
        
        try:
            result_mirror= list(zip(self.mirror_names, self.mirror_desc, self.mirror_dim, self.mirror_price_list))

            return result_mirror
        except (IndexError, TypeError):
            logging.warning("zip list of mirror is not created, check the conditions will affect mysql table")


        logging.info('Zipping all my lists in tuple: End')

