# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

xyxy = np.empty((0,4), int)

with open("input", "r") as file:
    for line in file:
        a, bc, d = line.split(sep=",")
        b, c = bc.split(sep=" -> ", )
        xyxy = np.append(xyxy, [[int(a), int(b), int(c), int(d)]], axis=0)


xym = (xyxy[:,0] == xyxy[:,2]) | (xyxy[:,1] == xyxy[:,3]) #alle diagonalen kicken
xyxy = xyxy[xym]

#feld mit nullen aufspannen, y spalten, xzeilen
logbuch = np.zeros((np.max(xyxy[:,0::2])+1,
                    np.max(xyxy[:,1::2])+1))

for coords in xyxy:
    if coords[0] <= coords[2] and coords[1] <= coords[3]: #x+ y+
        for x in range(coords[0],coords[2]+1,1):
            for y in  range(coords[1],coords[3]+1,1):
                logbuch[x,y] += 1
                
    if coords[0] > coords[2] and coords[1] <= coords[3]: #x- y+
        for x in range(coords[0],coords[2]-1,-1):
            for y in  range(coords[1],coords[3]+1,1):
                logbuch[x,y] += 1
                
    if coords[0] <= coords[2] and coords[1] > coords[3]: #x+ y-
        for x in range(coords[0],coords[2]+1,1):
            for y in  range(coords[1],coords[3]-1,-1):
                logbuch[x,y] += 1
                
    if coords[0] > coords[2] and coords[1] > coords[3]: #x- y-
        for x in range(coords[0],coords[2]-1,-1):
            for y in  range(coords[1],coords[3]-1,-1):
                logbuch[x,y] += 1
                
print(np.count_nonzero(logbuch>1))