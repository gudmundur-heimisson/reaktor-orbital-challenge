import re
import numpy as np
from satellite import Satellite

def parse_seed(seed_line):
    return float(re.match('^#SEED: (\d+\.\d+)$', seed_line).group(1))

def parse_satellite(sat_line):
    row = sat_line.split(',')
    ID = row[0]
    lat, lon = (np.deg2rad(float(x)) for x in row[1:3])
    alt = float(row[3])
    return Satellite(ID, lat, lon, alt)

def parse_route(route_line):
    row = [np.deg2rad(float(x)) for x in route_line.split(',')[1:]]
    start = np.array(row[:2])
    end = np.array(row[2:4])
    return start, end

def parse_data(raw_data):
    seed = parse_seed(raw_data[0])
    start, end = parse_route(raw_data[-1])
    satellites = []
    for line in raw_data[1:-1]:
        satellites.append(parse_satellite(line))
    return seed, satellites, start, end