'''
Created on May 9, 2016

@author: Gummi Heimisson
'''


class Satellite():

    # id is a reserved keyword, use ID instead
    def __init__(self, ID, lat, lon, alt):
        self.id = ID
        self.lat = lat
        self.lon = lon
        self.alt = alt
