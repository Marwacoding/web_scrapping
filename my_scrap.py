import re
import requests
from bs4 import BeautifulSoup #pour utiliser BeautifulSoup j'ai besoin de bs4
import logging


class Mycarpet() :

    logging.basicConfig(filename = "web_scrapping.log", 
    level= logging.INFO, format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')

    try:
        response = requests.get('https://www.maisonsdumonde.com/FR/fr/c/tapis-1559ac122904996dcae8be4c5de8fda6') #je prends les infos from mon url 
    except HTTPError:
        logging.info("Could not acces the URL")

#print(data.prettify()) #comme le pprint 

    def __init__(self):
        self.response = requests.get('https://www.maisonsdumonde.com/FR/fr/c/tapis-1559ac122904996dcae8be4c5de8fda6') #je prends les infos from mon url 
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
                #print(i.split(" - ")[1])
                #print('description without name = ',(i.split(" - ")))
                #print("type i = ", type(i)) == str

                description_sublist = re.split("(?<=\D)(?=\d)", i.split(" - ")[1], maxsplit=1)
    #             #print('this is description list", description_sublist') #== 2
                desc_item = [[item] for items in description_sublist for item in items.split(",")][0][0]
                self.desc.append(desc_item)
    #             print(description_sublist)
    #            print("final list of description ",self.desc)
        return self.desc

        logging.info("accessing carpet description -- End")

    def carpet_dim(self):
        logging.info("accessing carpet dimension -- Start")

    #         # #print(a.split("(?<=\D+)"))
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

        # print("this is name",self.names)
        # print("this is desc",self.desc)
        # print("this is dim",self.dim)
        # print("this is price",self.final_price)
        #print(self.names, self.desc, self.dim, self.final_price)
        result = list(zip(self.names, self.desc, self.dim, self.final_price))
        #self.result.append(r)
        #self.result= set(r)
        return result

        logging.info("ziping all list to tranfer db-- End")

    

#print(results)


    #my_carpets.final_list = zip(my_name, my_desc, my_dim, prices)
    
class Mirror(): 
    def __init__(self): 
        self.response_mirror = requests.get('https://www.maisonsdumonde.com/FR/fr/c/miroirs-484554f26aa42ef448cafd6fe7ad385e') #je prends les infos from mon url 
        self.maison_du_monde_mirror = self.response_mirror.text 
        self.data = BeautifulSoup(self.maison_du_monde_mirror,"html.parser")
        self.mirror_name_list = []
        self.mirror_price_list = []
        self.final_mirror = []

    def name_mirror(self):
        logging.info('Accessing my mirros name: start')
        mirror_name = []
        title_name = self.data.find_all("h2", class_= "font-weight-normal expand-link name mb-0")

        for k, item in enumerate(title_name):
            title = item.getText()
            mirror_name.append(title)
            self.mirror_name_list.append(mirror_name[k])
        return self.mirror_name_list
        #print(self.mirror_name_list)

        logging.info('Accessing my mirrors name: end')

    def price_mirror(self):
        logging.info('Getting my mirror price: start')
        mirror_price = []
        price_text = self.data.find_all("div", class_="ml-auto font-weight-semibold price")

        for k, item in enumerate(price_text): 
            price = item.getText()
            mirror_price.append(price)
            self.mirror_price_list.append(mirror_price[k].split()[0])
        return self.mirror_price_list
        #print(self.mirror_price_list)

        logging.info('Getting my carpets price: end')

    def zip_list_mirror(self):
        logging.info('Zipping all my lists in tuple: start')

        result_mirror= list(zip(self.mirror_name_list, self.mirror_price_list))
        #print("This is my result:" , result)

        return result_mirror

        logging.info('Zipping all my lists in tuple: end')

        #return self.final_mirror


