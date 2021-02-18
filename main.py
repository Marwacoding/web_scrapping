from my_scrap import *
#from file_db import *
#from file_db import *

print("hello")
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
print(prices)

results = my_carpets.zip_list()
#print(results)


my_mirror = Mirror()
mirror_total = my_mirror.name_mirror_total()
#print(mirror_total)

mirror_name = my_mirror.mirror_name()
#print(mirror_name)

mirror_desc = my_mirror.mirror_description()
#print(mirror_desc)

mirror_dim = my_mirror.mirror_dimention()
#print(mirror_dim)

mirror_price = my_mirror.price_mirror()
#print(mirror_price)

mirror_zip = my_mirror.zip_list_mirror()
#print(mirror_zip)


################################

# my_table = Table_carpet()
# create_my_db = my_table.create_db()
# #print(create_my_db)
# insert_to_db = my_table.read_from_db()
# #print(insert_to_db)