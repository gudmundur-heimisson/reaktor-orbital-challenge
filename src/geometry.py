'''
Created on May 9, 2016

@author: Gummi Heimisson
'''
import numpy as np

def polar(x, y, z):
    z2 = np.power(z, 2)
    r2 = np.power(x, 2) + np.power(y, 2) + z2
    r = np.sqrt(r2)
    t = np.arccos(x / np.sqrt(r2 - z2))
    p = np.arcsin(z / r)
    return np.array([r, t, p])

def cartesian(r, t, p):
    rcosp = r * np.cos(p)
    x = rcosp * np.cos(t)
    y = rcosp * np.sin(t)
    z = r * np.sin(p)
    return np.array([x, y, z])

def magnitude(X):
    return np.sqrt(sum(np.power(X, 2)))

def distance(X, Y):
    return magnitude(X - Y)

def closest_point(X, Y):
    a = np.power(Y, 2)
    b = np.power(X-Y, 2)
    c = X * Y
    L = -b + np.sqrt(np.power(b, 2) - 4*a*c) / 2*a
    if L >= 1:
        return X
    elif L <= 0:
        return Y
    else:
        return L*X + (1-L)*Y

