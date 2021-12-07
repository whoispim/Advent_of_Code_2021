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