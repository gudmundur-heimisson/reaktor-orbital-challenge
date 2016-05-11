'''
Created on May 10, 2016

@author: gummi
'''
from unittest import TestCase
from satellite import Satellite, line_of_sight
from math import pi, sqrt
import earth

class SatelliteTest(TestCase):

    def setUp(self):
        self.test_attrs = ['SAT0', 42, 3.4, 345]
        self.test_str = 'SAT0,42,3.4,345'
        self.sat = Satellite(*self.test_attrs)

    def test_init(self):
        sat = self.sat
        attrs = self.test_attrs
        self.assertListEqual(attrs, [sat.id, sat.lat, sat.lon, sat.alt])

    def test_str(self):
        sat = Satellite(*self.test_attrs)
        self.assertEqual(self.test_str, str(self.sat))

    def test_line_of_sight(self):
        sat1 = Satellite('SAT1', 0, 0, 1 + earth.radius * sqrt(2))
        sat2 = Satellite('SAT2', 0, pi, 1 + earth.radius * sqrt(2))
        self.assertFalse(line_of_sight(sat1, sat2))
        sat2.lon = pi/2
        self.assertTrue(line_of_sight(sat1, sat2))