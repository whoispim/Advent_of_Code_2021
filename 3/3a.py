# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 08:59:05 2021

@author: steska
"""

import numpy as np

data = np.genfromtxt("input", delimiter=1, dtype=int)

gam = 0b0
eps = 0b0

for i in range(data.shape[1]):
    if np.sum(data[:,i]) > data.shape[0]/2:
        gam = gam << 1 | 1
        eps = eps << 1 | 0
    else:
        gam = gam << 1 | 0
        eps = eps << 1 | 1
        
print(format(gam,"#014b"))
print(format(eps,"#014b"))
print(F"Power Consumption: {gam*eps}")