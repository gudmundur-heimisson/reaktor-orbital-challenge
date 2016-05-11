'''
Created on May 10, 2016

@author: gummi
'''

from requests import request
import parse_data as parse

URL = 'https://space-fast-track.herokuapp.com/generate'

def get_raw_data():
    r = request('GET', URL)
    return r.content.decode().strip().split('\n')

def get_data():
    return parse.parse_data(get_raw_data())
