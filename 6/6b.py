# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import time

with open("input","r") as f:
    fishies = [int(fish) for fish in f.readline().split(",")]

for day in range(256):
    start_time = time.time()
    print(F"Day {day}...")
    Neos = fishies.count(0)
    fishies = [6 if fish==0 else fish-1 for fish in fishies]
    for i in range(Neos):
        fishies.append(8)
    print("Done in %s seconds" % (time.time() - start_time))
    
print(F"Number of Fishies: {len(fishies)}")

#testfile: 
#Number of Fishies: 5934
#a  0.06827664375305176 seconds
#b  0.02988719940185547 seconds
#bb 0.0050122737884521484 seconds

#real input
#Number of Fishies: 359344
#a 48.101457357406616 seconds
#b 58.29901742935181 seconds
#bb 0.312028169631958 seconds