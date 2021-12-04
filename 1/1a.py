# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 08:59:05 2021

@author: steska
"""

import numpy as np

data = np.genfromtxt("input")

temp=0
count=0
for i, zahl in enumerate(data):
    if i > 0:
       if zahl>temp:
           count+=1
    temp=zahl
        
print(count)