'''
Created on May 10, 2016

@author: gummi
'''

from unittest import TestCase
from satellite import Satellite
from math import pi, sqrt
import earth

class SatelliteTest(TestCase):

    def test_sees(self):
        sat1 = Satellite('SAT1', 0, 0, 1 + earth.radius * sqrt(2))
        sat2 = Satellite('SAT2', 0, pi, 1 + earth.radius * sqrt(2))
        sat3 = Satellite('SAT2', 0, pi/2, 1 + earth.radius * sqrt(2))
        self.assertFalse(sat1.sees(sat2))
        self.assertTrue(sat1.sees(sat3))
        self.assertTrue(sat2.sees(sat3))
