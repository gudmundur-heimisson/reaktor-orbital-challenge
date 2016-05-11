'''
Created on May 9, 2016

@author: Gummi Heimisson
'''

import numpy as np
import geometry as geom
import earth

class Satellite():

    # id is a reserved keyword, use ID instead
    def __init__(self, ID, lat, lon, alt):
        self.id = ID
        self.lat = lat
        self.lon = lon
        self.alt = alt

    def __eq__(self, other):
        attrs = ['id', 'lat', 'lon', 'alt']
        return all(getattr(self, attr) == getattr(other, attr) for attr in attrs)

    def __str__(self):
        return ','.join(str(attr) for attr in
                        [self.id, self.lat, self.lon, self.alt])


def line_of_sight(sat1, sat2):
    R1 = np.array([earth.radius + sat1.alt, sat1.lon, sat1.lat])
    R2 = np.array([earth.radius + sat2.alt, sat2.lon, sat2.lat])
    X1, X2 = geom.cartesian(*R1), geom.cartesian(*R2)
    return geom.magnitude(geom.tangent_point(X1, X2)) > earth.radius