'''
Created on May 10, 2016

@author: gummi
'''

import numpy as np
from unittest.case import TestCase
from os.path import dirname, join
from satellite import Satellite
import parse_data as parse

class ParseTest(TestCase):

    def setUp(self):
        test_input_dir = dirname(__file__)
        test_filename = join(test_input_dir, 'test_data.csv')
        with open(test_filename, 'r') as test_file:
            self.raw_data = test_file.readlines()
        self.test_seed = 0.1582549053709954
        self.test_sat = Satellite('SAT0',
                                  np.deg2rad(88.21823276533055),
                                  np.deg2rad(-50.97929950467153),
                                  690.1774276106411)
        self.start = np.array([np.deg2rad(-32.958519580214514),
                               np.deg2rad(71.85325246833762)])
        self.end = np.array([np.deg2rad(3.2540908414234764),
                             np.deg2rad(2.5430169084402507)])

    def test_parse_seed(self):
        seed_line = self.raw_data[0]
        seed = parse.parse_seed(seed_line)
        print('seed: ', seed)
        self.assertEqual(seed, self.test_seed)

    def test_parse_satellite(self):
        sat_line = self.raw_data[1]
        sat = parse.parse_satellite(sat_line)
        print('sat: ', sat)
        self.assertEqual(sat, self.test_sat)

    def test_parse_route(self):
        route_line = self.raw_data[-1]
        start, end = parse.parse_route(route_line)
        print("start: ", start)
        print("end: ", end)
        self.assertListEqual(list(start), list(self.start))
        self.assertListEqual(list(end), list(self.end))

    def test_parse_data(self):
        seed, sats, start, end = parse.parse_data(self.raw_data)
        self.assertEqual(seed, self.test_seed)
        self.assertEqual(len(sats), 20)
        self.assertEqual(sats[0], self.test_sat)
        self.assertListEqual(list(start), list(self.start))
        self.assertListEqual(list(end), list(self.end))
