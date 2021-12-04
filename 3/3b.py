# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 08:59:05 2021

@author: steska
"""

import numpy as np

data = np.genfromtxt("input", delimiter=1, dtype=int)

def bitcrit(rest): #use code from last exercise to find most and lest appearing bit for each column
    gam = 0b0
    eps = 0b0
    for i in range(rest.shape[1]):
        if np.sum(rest[:,i]) >= rest.shape[0]/2:
            gam = gam << 1 | 1 #move whole bitstring to the left by one, then add 1
            eps = eps << 1     #move whole bitstring to the left by one, leaving a 0
        else:
            gam = gam << 1 
            eps = eps << 1 | 1
    return gam, eps

what = data
whatmask = []
j = 0
while True:
    gam, eps = bitcrit(what)
    whatmask = what[:,j] == gam >> data.shape[1]-j-1 & 1 #move interesting bit to rightmost position, compare with 1, then mask accordingly
    what = what[whatmask] #apply mask
    if what.shape[0] == 1: #stop if only one row is left
        break
    j += 1 #next column
oxy = what

what = data
whatmask = []
j = 0
while True:
    gam, eps = bitcrit(what)
    whatmask = what[:,j] == eps >> data.shape[1]-j-1 & 1 #move interesting bit to rightmost position, compare with 1, then mask accordingly
    what = what[whatmask] #apply mask
    if what.shape[0] == 1: #stop if only one row is left
        break
    j += 1 #next column
co2 = what

oxyb=0
co2b=0
for bit in oxy[0]:
    oxyb = oxyb << 1 | bit
for bit in co2[0]:
    co2b = co2b << 1 | bit

print(F"Oxygen:              {format(oxyb,'#014b')}")
print(F"CO2:                 {format(co2b,'#014b')}")
print(F"Life Support Rating: {oxyb*co2b}")