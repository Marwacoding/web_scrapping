import unittest
import os

from my_scrap import Mycarpet
from my_scrap import  Mirror

#https://stackoverflow.com/questions/33216488/is-there-any-way-to-check-with-python-unittest-assert-if-an-iterable-is-not-empt

class Testing_scrap(unittest.TestCase):

    def test_carpet_all_item(self):
        test_carpet= Mycarpet()
        test_carpet.carpet()
        self.assertTrue(len(test_carpet.final_item) > 0)
    
    # def test_name_carpet(self):
    #     test_carpet= Mycarpet()
    #     test_carpet.carpet_name()
    #     self.assertTrue(len(test_carpet.names) > 0)
    
    # def test_desc_carpet(self):
    #     test_carpet= Mycarpet()
    #     test_carpet.carpet_desc()
    #     self.assertTrue(len(test_carpet.desc) > 0)
    
    # def test_carpet_dim(self):
    #     test_carpet= Mycarpet()
    #     test_carpet.carpet_dim()
    #     self.assertTrue(len(test_carpet.dim) > 0)
    
    # def test_carpet_dates(self):
    #     test_carpet = Mycarpet()
    #     test_carpet.carpet_dates()
    #     self.assertTrue(len(test_carpet.carpet_date) > 0)

    def test_carpet_price_list(self): 
        test_carpet= Mycarpet()
        test_carpet.carpet_price()
        self.assertTrue(len(test_carpet.final_price) >  0)

    def test_mirror_all_item(self):
        test_mirror= Mirror()
        test_mirror.name_mirror_total()
        self.assertTrue(len(test_mirror.mirror_name_list) > 0)

    def test_mirror_price_list(self):
        test_mirror= Mirror()
        test_mirror.price_mirror()
        self.assertTrue(len(test_mirror.mirror_price_list) > 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)