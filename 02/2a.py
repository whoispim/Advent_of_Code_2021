import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_csv("input", 
                   header=None, 
                   dtype={"richt" : str, "dist" : int}, 
                   sep = " ")

depth, horid = 0, 0

coords = np.array([[0, 0]])

for index, row in data.iterrows():
    if row[0] == "forward":
        horid += row[1]
    if row[0] == "up":
        depth -= row[1]
    if row[0] == "down":
        depth += row[1]
    coords = np.append(coords,[[depth, horid]], axis=0)
    
plt.scatter(coords[:,1], -coords[:,0])
plt.title("2a")
plt.xlabel("Distanz")
plt.ylabel("Tiefe")

plt.savefig("2a.png")

print(F"Tiefe: {depth}, Horizontale Distanz: {horid}, Produkt: {depth*horid}")
