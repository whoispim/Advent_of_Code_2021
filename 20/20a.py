import time
start_time = time.time()

import numpy as np
from io import StringIO

def apply_algo(submat, algorithm):
    bintrack = 0
    for x in submat.flatten():
        bintrack = bintrack * 2 + x
    return algo[bintrack]

with open("input") as f:
    algo, pictxt = f.read().replace(".","0").replace("#","1").split("\n\n")

pic = np.genfromtxt(StringIO(pictxt), delimiter=1, dtype="int")
 # pad once with zero, then use edge to account for infinity
pic = np.pad(pic, pad_width=1, mode="constant")
startshape = pic.shape

for i in range(50):
    pic = np.pad(pic, pad_width=3, mode="edge")
    newpic = np.zeros(pic.shape, dtype="int")
    
    for row in range(1, pic.shape[0] - 1):
        for col in range(1, pic.shape[1] - 1):
            newpic[row,col] = apply_algo(pic[row-1:row+2,col-1:col+2], algo)
        
    pic = newpic[2:-2,2:-2]
    
    print(F"There are {np.sum(pic)} lit pixels after {i+1} iterations")

print()
print("--- %s seconds ---" % (time.time() - start_time))
