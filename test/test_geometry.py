'''
Created on May 9, 2016

@author: Gummi Heimisson
'''

from unittest import TestCase
from math import pi, sqrt
import numpy as np
import geometry as geo


class GeometryTest(TestCase):

    def error(self, x, y):
        return np.sum(np.abs(x - y))

    def setUp(self):
        self.X = np.array([sqrt(3)/2, 3/2, 1])
        self.R = np.array([2, pi/3 , pi/6])
        print("X: ", self.X)
        print("R: ", self.R)

    def test_polar(self):
        X_p = geo.polar(*self.X)
        print("X_p: ", X_p)
        self.assertAlmostEqual(self.error(X_p, self.R), 0)

    def test_cartesian(self):
        R_c = geo.cartesian(*self.R)
        print("R_c:", R_c)
        self.assertAlmostEqual(self.error(R_c, self.X), 0)

    def test_magnitude(self):
        r = geo.magnitude(self.X)
        print("r: ", r)
        self.assertAlmostEqual(self.R[0], r)

    def test_distance(self):
        X2 = np.array(self.X)
        X2[2] = 0
        dist = geo.distance(self.X, X2)
        print("Dist: ", dist)
        self.assertAlmostEqual(dist, self.X[2])

    def test_tangent_point(self):
        x = np.array([1, 0])
        y = np.array([0, 1])
        tp = geo.tangent_point(x, y)
        tp_actual = np.array([0.5, 0.5])
        print("tp: ", tp)
        self.assertAlmostEqual(self.error(tp, tp_actual), 0)
        x = np.array([0.1, 0.1])
        y = np.array([0, 1])
        tp = geo.tangent_point(x, y)
        print("tp: ", tp)
        self.assertAlmostEqual(self.error(tp, x), 0)
