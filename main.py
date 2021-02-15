import re
import requests
from bs4 import BeautifulSoup #pour utiliser BeautifulSoup j'ai besoin de bs4

response = requests.get('https://www.maisonsdumonde.com/FR/fr/c/tapis-1559ac122904996dcae8be4c5de8fda6') #je prends les infos from mon url 

maison_du_monde = response.text 
data = BeautifulSoup(maison_du_monde,"html.parser") #permet de récupérer la data de ma page sous forme HTML 

#print(data.prettify()) #comme le pprint 

carpet_list = []
final_item = []
names = []
desc = []
dim = []

def carpet():
    title_item = data.find_all("h2", class_= "font-weight-normal expand-link name mb-0")
    
    for k, item in enumerate(title_item):
        title = item.getText()
        carpet_list.append(title)
        final_item.append(carpet_list[k])
    #print('this is carpet info', final_item)
    return final_item

my_carpet = carpet()
#print(my_carpet)


def carpet_name():
    for i in my_carpet:
        names.append(i.split(" - ")[0])
        #print(type(names))
        #print('name of carptet = ',names)
    return names
    
my_carpet_name = carpet_name()
#print(my_carpet_name)


def carpet_desc():
    for i in my_carpet:
        if len(i.split(" - "))==2:
            #print(i.split(" - ")[1])
            #print('description without name = ',(i.split(" - ")))
            #print("type i = ", type(i)) == str


             description_sublist = re.split("(?<=\D)(?=\d)", i.split(" - ")[1], maxsplit=1)
#             #print('this is description list", description_sublist') #== 2
             desc_item = [[item] for items in description_sublist for item in items.split(",")][0][0]
             desc.append(desc_item)
#             #print(description_sublist)
#             #print("final list of description ",desc)
    return desc

my_desc = carpet_desc()
#print(my_desc)

def carpet_dim():
#         # #print(a.split("(?<=\D+)"))
    for i in my_carpet:
         dim_item =re.split("(?<=\D)(?=\d)", i, maxsplit= 1)[1]
         dim.append(dim_item)
    return dim

my_dim=carpet_dim()
#print(my_dim)

#         #print('this is the final dimension',dim)
#     #print(name, desc, dim)
#         #final_list = list(zip(name, desc, dim))
#         #print(final_list)

#     result = zip(names, desc, dim)
#     print(result)
#     return names, desc, dim

# carpet_name()



item_list = []
final_price = []

def carpet_price():
    item_price = data.find_all("div", class_= "ml-auto font-weight-semibold price")
    #print(item_price)


    for k, item in enumerate(item_price):
        price = item.getText()
        item_list.append(price)
        #final_price.append(item_list[k])
        final_price.append(item_list[k].split()[0])

    return final_price

prices = carpet_price()
#<div class="ml-auto font-weight-semibold price"><span>79,99&nbsp;€</span> <!----></div>

#print(final_price)