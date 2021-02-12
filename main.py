from typing import final
import requests
from bs4 import BeautifulSoup #pour utiliser BeautifulSoup j'ai besoin de bs4

response = requests.get('https://www.maisonsdumonde.com/FR/fr/c/tapis-1559ac122904996dcae8be4c5de8fda6') #je prends les infos from mon url 

maison_du_monde = response.text 
data = BeautifulSoup(maison_du_monde,"html.parser") #permet de récupérer la data de ma page sous forme HTML 

#print(data.prettify()) #comme le pprint 

carpet_list = []
final_item = []


def carpet_name():
    title_item = data.find_all("h2", class_= "font-weight-normal expand-link name mb-0")

    for k, item in enumerate(title_item):
        title = item.getText()
        carpet_list.append(title)
        final_item.append(carpet_list[k])
    
    return final_item

    #print(final_item)

carpet_name()


def carpet_price():
    item_price = data.find_all("div", class_= "ml-auto font-weight-semibold price")
    #print(item_price)
    item_list = []
    final_price = []

    for k, item in enumerate(item_price):
        price = item.getText()
        item_list.append(price)
        #final_price.append(item_list[k])
        final_price.append(item_list[k].split()[0])

    return final_price

carpet_price()
#<div class="ml-auto font-weight-semibold price"><span>79,99&nbsp;€</span> <!----></div>