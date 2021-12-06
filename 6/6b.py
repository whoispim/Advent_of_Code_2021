# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import time
start_time = time.time()

fishies = np.genfromtxt("inputtest", delimiter=",", dtype="int")

for day in range(80):
    fishies -= 1
    fishmask = fishies < 0
    fishies [fishmask] = 6
    for i in range(np.count_nonzero(fishmask)):
        fishies = np.append(fishies, 8)
            
print(F"Number of Fishies: {len(fishies)}")
print(" %s seconds" % (time.time() - start_time))

#testfile: 
#Number of Fishies: 5934
#a 0.06827664375305176 seconds
#b 0.02988719940185547 seconds

#real input
#Number of Fishies: 359344
#a 48.101457357406616 seconds
#b 58.29901742935181 seconds