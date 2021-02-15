import re
import requests
from bs4 import BeautifulSoup #pour utiliser BeautifulSoup j'ai besoin de bs4

response = requests.get('https://www.maisonsdumonde.com/FR/fr/c/tapis-1559ac122904996dcae8be4c5de8fda6') #je prends les infos from mon url 

maison_du_monde = response.text 
data = BeautifulSoup(maison_du_monde,"html.parser") #permet de récupérer la data de ma page sous forme HTML 

#print(data.prettify()) #comme le pprint 


class Mycarpet() :
    def __init__(self):
        self.carpet_list = []
        self.final_item = []
        self.names = []
        self.desc = []
        self.dim = []
        self.item_list = []
        self.final_price = []
        self.result = []

        
    def carpet(self):
        title_item = data.find_all("h2", class_= "font-weight-normal expand-link name mb-0")
        
        for k, item in enumerate(title_item):
            title = item.getText()
            self.carpet_list.append(title)
            self.final_item.append(self.carpet_list[k])
        #print('this is carpet info', final_item)
        

#print(my_carpet)
 

    def carpet_name(self):
        for i in self.final_item:
            #print(i)
            if len(i.split(" - "))==2:
                self.names.append(i.split(" - ")[0])
            #print('name of carptet  1= ',self.names)
        return self.names
        

    #print(my_carpet_name)


    def carpet_desc(self):
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


#print(my_desc)

    def carpet_dim(self):
    #         # #print(a.split("(?<=\D+)"))
        for i in self.final_item:
            if len(i.split(" - "))==2:
                dim_item =re.split("(?<=\D)(?=\d)", i, maxsplit= 1)[1]
                self.dim.append(dim_item)
    
        return self.dim
    

#print(my_dim)

#         #print('this is the final dimension',dim)
#     #print(name, desc, dim)
#         #final_list = list(zip(name, desc, dim))
#         #print(final_list)

#     result = zip(names, desc, dim)
#     print(result)
#     return names, desc, dim

# carpet_name()


    def carpet_price(self):
        item_price = data.find_all("div", class_= "ml-auto font-weight-semibold price")
        #print(item_price)


        for k, item in enumerate(item_price):
            price = item.getText()
            self.item_list.append(price)
            #final_price.append(item_list[k])
            self.final_price.append(self.item_list[k].split()[0])
        return self.final_price



#<div class="ml-auto font-weight-semibold price"><span>79,99&nbsp;€</span> <!----></div>

#print(final_price)

    def zip_list(self): 
        # print("this is name",self.names)
        # print("this is desc",self.desc)
        # print("this is dim",self.dim)
        # print("this is price",self.final_price)
        #print(self.names, self.desc, self.dim, self.final_price)
        result = list(zip(self.names, self.desc, self.dim, self.final_price))
        #self.result.append(r)
        #self.result= set(r)
        return result

    


#if __name__ == '__main__':
my_carpets = Mycarpet()
item= my_carpets.carpet()
my_name = my_carpets.carpet_name()
#print(my_name)
my_desc = my_carpets.carpet_desc()
#print(my_desc)
my_dim = my_carpets.carpet_dim()
#print(my_dim)
prices = my_carpets.carpet_price()
#print(prices)
results = my_carpets.zip_list()
print(results)


    #my_carpets.final_list = zip(my_name, my_desc, my_dim, prices)
    
