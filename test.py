import unittest
import os

from my_scrap import Mycarpet, Mirror

#https://stackoverflow.com/questions/33216488/is-there-any-way-to-check-with-python-unittest-assert-if-an-iterable-is-not-empt

class TestStringMethods(unittest.TestCase):
    
    def test_connection(self):
        my_carpet = Mycarpet()
        read_api_class.save_my_json()
        read_api_class.request_JSON()
        self.assertTrue(os.path.isfile("marwa_sncf.json"))
        self.assertEquals(type(read_api_class.raw_data), dict)
        self.assertIn('links', read_api_class.raw_data.keys())
        self.assertIn('href', read_api_class.raw_data['links'][0].keys())
        #self.assertIn('stop_areas', read_api_class.raw_data["stop_areas"][0])
    

    def test_def_my_endpoints_list(self):  
        test_my_endpoints_element = ReadingSncfApi()
        test_my_endpoints_element.request_JSON()
        test_my_endpoints_element.my_endpoints()
        self.assertTrue(len(test_my_endpoints_element.my_endpoints_list) > 0)


    def test_def_my_id_list(self):
        test_my_id = ReadingSncfApi()
        test_my_id.request_JSON()
        test_my_id.my_id()
        self.assertTrue(len(test_my_id.my_id_list) > 0)


    def test_my_station_name_list(self):
        test_my_station = ReadingSncfApi()
        test_my_station.request_JSON()
        test_my_station.my_station_name()
        self.assertTrue(len(test_my_station.my_list_station) > 0)
   

    def test_def_my_coord_list(self):
        test_my_coord = ReadingSncfApi()
        test_my_coord.request_JSON()
        test_my_coord.my_coord()
        self.assertTrue(len(test_my_coord.my_list_coord) > 0)


    def test_my_csv_station(self):
        test_csv_station = ReadingSncfApi()
        test_csv_station.request_JSON()
        test_csv_station.csv_station()
        self.assertTrue(os.path.isfile("my_gare.csv"))
        self.assertTrue(('id' and 'name' and 'coord'), test_csv_station.data.keys())
    

    def test_my_csv_endpoints(self):
        test_csv_endpoints = ReadingSncfApi()
        test_csv_endpoints.request_JSON()
        test_csv_endpoints.csv_endpoints()
        self.assertTrue(os.path.isfile("my_links.csv"))
        self.assertTrue('endpoints', test_csv_endpoints.links.keys())


    def test_my_request_api_paris_lyon(self):
        test_request_paris_lyon = ReadingSncfApi()
        test_request_paris_lyon.request_api_paris_lyon()
        test_request_paris_lyon.save_my_paris_lyon_json()
        self.assertTrue(os.path.isfile("m_sncf.json"))
        self.assertEquals(type(test_request_paris_lyon.data_journey), dict)
        self.assertIn('journeys', test_request_paris_lyon.data_journey.keys())
        self.assertTrue(len(test_request_paris_lyon.data_journey["journeys"][0]) > 0)
        self.assertIn("sections", test_request_paris_lyon.data_journey["journeys"][0].keys())
        self.assertIn("stop_date_times", test_request_paris_lyon.data_journey["journeys"][0]["sections"][1])


    def test_nb_tranfers(self):
        test_my_tranfers = ReadingSncfApi()
        test_my_tranfers.request_api_paris_lyon()
        test_my_tranfers.nbr_of_train_change()
        self.assertTrue(len(test_my_tranfers.transfers_list) > 0)


    def test_collecting_station_name(self):
        test_collecting_stations = ReadingSncfApi()
        test_collecting_stations.request_api_paris_lyon()
        test_collecting_stations.collectiong_station_name()
        self.assertTrue(len(test_collecting_stations.stop_list) > 0)
        self.assertNotEqual(test_collecting_stations.stop_time, 0)
   


if __name__ == '__main__':
    unittest.main(verbosity=2)