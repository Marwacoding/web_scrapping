import re
import requests
from bs4 import BeautifulSoup #pour utiliser BeautifulSoup j'ai besoin de bs4
import logging


try:
    response = requests.get('https://www.maisonsdumonde.com/FR/fr/c/tapis-1559ac122904996dcae8be4c5de8fda6', verify=False)
except requests.exceptions.ConnectionError:
    logging.info("failed to access url")



class Mycarpet() :

    logging.basicConfig(filename = "web_scrapping.log", 
    level= logging.INFO, format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')


    def __init__(self):
        
        self.response = requests.get('https://www.maisonsdumonde.com/FR/fr/c/tapis-1559ac122904996dcae8be4c5de8fda6', timeout=5, verify=False) 
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
        #try:
        for k, item in enumerate(title_item):
            title = item.getText()
            carpet_list.append(title)
            self.final_item.append(carpet_list[k])
        
        logging.info("accessing carpet info -- End")
            #return 
        #except:
        #    print("hello")
        #print('this is carpet info', final_item)
        

    def carpet_name(self):
        logging.info("accessing carpet name -- Start")

        for i in self.final_item:
            #print(i)
            if len(i.split(" - "))==2:
                self.names.append(i.split(" - ")[0])
            #print('name of carptet  1= ',self.names)
        return self.names

        logging.info("accessing carpet name -- End")
        

    def carpet_desc(self):
        logging.info("accessing carpet description -- Start")


        for i in self.final_item:
            if len(i.split(" - "))==2:
                description_sublist = re.split("(?<=\D)(?=\d)", i.split(" - ")[1], maxsplit=1)
                desc_item = [[item] for items in description_sublist for item in items.split(",")][0][0]
                self.desc.append(desc_item)

        return self.desc


    def carpet_dim(self):
        logging.info("accessing carpet dimention -- Start")


        for i in self.final_item:
            if len(i.split(" - "))==2:
                dim_item =re.split("(?<=\D)(?=\d)", i, maxsplit= 1)[1]
                self.dim.append(dim_item)
    
        return self.dim


    def carpet_price(self):
        logging.info("accessing carpet price -- Start")

        item_price = self.data.find_all("div", class_= "ml-auto font-weight-semibold price")
        #print(item_price)

        item_list = []

        for k, item in enumerate(item_price):
            price = item.getText()
            item_list.append(price)
            #final_price.append(item_list[k])
            self.final_price.append(item_list[k].split()[0])
        return self.final_price

        logging.info("accessing carpet price -- End")


    def zip_list(self): 
        logging.info("ziping all list to tranfer db-- Start")

        #print("this is name",self.names)
        #print("this is desc",self.desc)
        #print("this is dim",self.dim)
        #print("this is price",self.final_price)
        #print(self.names, self.desc, self.dim, self.final_price)
        result = list(zip(self.names, self.desc, self.dim, self.final_price))
        #self.result.append(r)
        
        return result

        logging.info("ziping all list to tranfer db-- End")

        
class Mirror(): 
    def __init__(self): 
        self.response_mirror = requests.get('https://www.maisonsdumonde.com/FR/fr/c/miroirs-484554f26aa42ef448cafd6fe7ad385e', timeout=5, verify=False) #je prends les infos from mon url 
        self.maison_du_monde_mirror = self.response_mirror.text 
        self.data = BeautifulSoup(self.maison_du_monde_mirror,"html.parser")
        
        self.mirror_name_list = []
        self.mirror_names = []
        self.mirror_desc = []
        self.mirror_dim = []
        self.mirror_price_list = []
        self.final_mirror = []

    def name_mirror_total(self):
        logging.info('Accessing mirros name: start')
        mirror_name = []
        title_name = self.data.find_all("h2", class_= "font-weight-normal expand-link name mb-0")

        for k, item in enumerate(title_name):
            title = item.getText()
            mirror_name.append(title)
            self.mirror_name_list.append(mirror_name[k])
        return self.mirror_name_list

        logging.info('Accessing mirrors name: end')

    

    def mirror_name(self):
        logging.info("accessing mirror name -- Start")

        for i in self.mirror_name_list:
            #print(i)
            if len(i.split(" - "))==2:
                self.mirror_names.append(i.split(" - ")[0])
        return self.mirror_names

        logging.info("accessing mirror name -- End")



    def mirror_description(self):
        logging.info("accessing mirror description -- Start")


        for i in self.mirror_name_list:
            if len(i.split(" - "))==2:
                description_sublist = re.split("(?<=\D)(?=\d)", i.split(" - ")[1], maxsplit=1)
                desc_item = [[item] for items in description_sublist for item in items.split(",")][0][0]
                self.mirror_desc.append(desc_item)

        return self.mirror_desc

        logging.info("accessing mirror description -- End")
    


    def mirror_dimention(self):
        logging.info("accessing mirror dimension -- Start")

        for i in self.mirror_name_list:
            if len(i.split(" - "))==2:
                dim_item =re.split("(?<=\D)(?=\d)", i, maxsplit= 1)[1]
                self.mirror_dim.append(dim_item)
    
        return self.mirror_dim
        logging.info("accessing mirror dimension -- End")



    def price_mirror(self):
        logging.info('Getting my mirror price: start')
        mirror_price = []
        price_text = self.data.find_all("div", class_="ml-auto font-weight-semibold price")

        for k, item in enumerate(price_text): 
            price = item.getText()
            mirror_price.append(price)
            self.mirror_price_list.append(mirror_price[k].split()[0])
        return self.mirror_price_list

        logging.info('Getting my carpets price: end')

    

    def zip_list_mirror(self):
        logging.info('Zipping all my lists in tuple: start')

        result_mirror= list(zip(self.mirror_names, self.mirror_desc, self.mirror_dim, self.mirror_price_list))

        return result_mirror

        logging.info('Zipping all my lists in tuple: end')

