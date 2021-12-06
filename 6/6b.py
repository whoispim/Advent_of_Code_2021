# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time

with open("inputtest","r") as f:
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
