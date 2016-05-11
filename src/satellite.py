'''
Created on May 9, 2016

@author: Gummi Heimisson
'''

import numpy as np
from geometry import magnitude, tangent_point, cartesian
import earth

class Satellite():

    # id is a reserved keyword, use ID instead
    def __init__(self, ID, lat, lon, alt):
        self.id = ID
        self._R = np.array([alt, lon, lat], dtype='float_')
        self._X = cartesian(*self._R)

    def __eq__(self, other):
        attrs = ['id', 'lat', 'lon', 'alt']
        return all(getattr(self, attr) == getattr(other, attr) for attr in attrs)

    def __str__(self):
        return ','.join(str(attr) for attr in
                        [self.id, np.rad2deg(self.lat), np.rad2deg(self.lon), self.alt])

    @property
    def alt(self):
        return self._R[0]

    @property
    def lon(self):
        return self._R[1]

    @property
    def lat(self):
        return self._R[2]


    def sees(self, other):
        return magnitude(tangent_point(self._X, other._X)) > earth.radius


