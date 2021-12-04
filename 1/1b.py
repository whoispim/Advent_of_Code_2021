# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 08:59:05 2021

@author: steska
"""

import numpy as np

data = np.genfromtxt("input")

temp=0
count=0

for i in range(data.size-2):
    if i > 0:
        temp1 = data[i] + data[i+1] + data[i+2]
        if temp1 > temp:
            count += 1        
    temp = data[i] + data[i+1] + data[i+2]
        
print(count)