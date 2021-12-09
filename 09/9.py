import time
start_time = time.time()
import numpy as np
from scipy import ndimage

def find_low(inmap):
    lowp = np.empty((0,2), dtype="int")
    for i in range(hmap.shape[0]):
        for j in range(hmap.shape[1]):
            if ((i==0 or inmap[i,j] < inmap[max(i-1,0), j]) and
                (j==0 or inmap[i,j] < inmap[i, max(j-1,0)]) and
                (i==inmap.shape[0]-1 or inmap[i,j] < inmap[min(i+1,inmap.shape[0]-1), j]) and
                (j==inmap.shape[1]-1 or inmap[i,j] < inmap[i, min(j+1,inmap.shape[1]-1)])):
                lowp = np.append(lowp, [[i,j]], axis=0)
    return lowp

def get_height(inmap,lowp):
    output = []
    for i,j in lowp:
        output.append(inmap[i,j])
    return output

def get_risk(hei):
    output = 0
    for x in hei:
        output += x + 1
    return output

def get_poolsize(ar, nar):
    output = []
    for x in range(1,nar+1):
        output.append(np.count_nonzero(ar == x))
    return output

hmap = np.genfromtxt("input", dtype="int", delimiter=1)

low_points = find_low(hmap)
heights = get_height(hmap,low_points)

print(F"Risk point heights: {heights}")
print(F"Total risk level: {get_risk(heights)}")

borders = hmap != 9
areas, nareas = ndimage.label(borders)

pools = get_poolsize(areas, nareas)
pools.sort()
print()
print(F"Number of Basins: {nareas}")
print(F"Size of biggest three: {pools[-3:]}")
print(F"Product: {pools[-3] * pools[-2] * pools[-1]}")

print()
print("--- %s seconds ---" % (time.time() - start_time))
