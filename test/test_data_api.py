'''
Created on May 10, 2016

@author: Gummi Heimisson
'''

from unittest import TestCase
import data_api as api

class DataAPITest(TestCase):

    def test_get_raw_data(self):
        raw_data = api.get_raw_data()
        print('raw_data: ')
        print(*raw_data, sep='\n')
        self.assertEqual(len(raw_data), 22)
