from my_scrap import *

if __name__ == '__main__':
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


    my_mirror = Mirror()
    mirror_name = my_mirror.name_mirror()
    #print(mirror_name)

    mirror_price = my_mirror.price_mirror()
    #print(mirror_price)

    mirror_zip = my_mirror.zip_list_mirror()
    #print(mirror_zip)