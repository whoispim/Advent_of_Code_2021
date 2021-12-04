# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 08:59:05 2021

@author: steska
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_csv("input", 
                   header=None, 
                   dtype={"richt" : str, "dist" : int}, 
                   sep = " ")

aim, depth, horid = 0, 0, 0

coords = np.array([[0, 0]])

for index, row in data.iterrows():
    if row[0] == "up":
        aim -= row[1]
    if row[0] == "down":
        aim += row[1]
    if row[0] == "forward":
        horid += row[1]
        depth += row[1] * aim
    coords = np.append(coords,[[depth, horid]], axis=0)
    
plt.scatter(coords[:,1], -coords[:,0])
plt.title("2b")
plt.xlabel("Distanz")
plt.ylabel("Tiefe")

#scientific notation
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0E}'.format(x) for x in current_values])

plt.savefig("2b.png")

print(F"Tiefe: {depth}, Horizontale Distanz: {horid}, Produkt: {depth*horid}")
