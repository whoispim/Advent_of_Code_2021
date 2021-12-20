import time
start_time = time.time()

import numpy as np
import numpy_indexed as npi
from io import StringIO
from collections import Counter

def rotate(mat, ax, repetitions=1):
    el_rot = [[[ 1, 0, 0],
               [ 0, 0,-1], #x
               [ 0, 1, 0]],
              [[ 0, 0, 1],
               [ 0, 1, 0], #y
               [-1, 0, 0]],
              [[ 0,-1, 0],
               [ 1, 0, 0], #z
               [ 0, 0, 1]]]
    for i in range(repetitions):
        mat = np.dot(mat, el_rot[ax])
    return mat

def orientate(target, mat):
    wow = False
    for i, matrix in enumerate(rotmats):
        rmat = np.dot(mat, matrix)
        if check(target, rmat):
            wow = True
            break
    if wow:
        return i
    else:
        return -1

def check(target, mat):
    distlist = []
    for i in range(target.shape[0]):
        for j in range(mat.shape[0]):
            distlist.append(np.linalg.norm(target[i] - mat[j]))
    # print(str(Counter(distlist).most_common(1)[0][1]) + " ", end="")
    if (Counter(distlist).most_common(1)[0][1]) >=12:
        return True
    return False

def build_chains(matchgrid):
    cha = []
    for i, scanner in enumerate(matchgrid):
        ch = []
        for j, partner in enumerate(scanner):
            if i != j:
                if partner >=0:
                    ch.append(j)
        cha.append(ch)
        
    connected = {0:0}
    while len(connected) < 40:
        for i in list(set(range(40)) - set(connected.keys())): #all unconnected
            for j in cha[i]:
                if j in connected:
                    connected[i] = j
#        print(connected)
        
    return connected

def unwonkyfy(sca, connected, matchgrid, rotm):
    oriented = []
    for i, scan in enumerate(sca):
        pos = i
        while pos != 0:
            buddy = connected[pos]
            scan = np.dot(scan,rotm[matchgrid[buddy][pos]])
            pos = buddy
        oriented.append(scan)
    return oriented

def overlap(sca, connected): # ???????
    overlapped = []
    movelist = [0] * 40
    total_movelist = np.zeros((40,3))
    for i in range(40):
        buddy = connected[i]
        source = sca[i]
        target = sca[buddy]
        veclist = []
        for p_s in source:
            for p_t in target:
                veclist.append(np.subtract(p_t,p_s))
        movelist[i] = npi.mode(veclist)
    for i in range(40):
        pos = i
        mod_me = sca[i]
#        print(F"Starting with {i}")
        while pos != 0:
#            print(F"--I am at {pos}")
            mod_me = np.add(mod_me, movelist[pos])
            total_movelist[i] = np.add(total_movelist[i], movelist[pos])
#            print(F"----{movelist[pos]}")
#            print(F"----{total_movelist[i]}")
            pos = connected[pos]
        overlapped.append(mod_me)
    return overlapped, total_movelist
            
def find_max_distance(movelist):
    maxi = 0
    for i, vec_i in enumerate(movelist[:-1]):
        for vec_j in movelist[i+1:]:
            dist_vec = np.subtract(vec_i, vec_j)
            taxi = (abs(dist_vec[0]) +
                    abs(dist_vec[1]) +
                    abs(dist_vec[2]))
#            print(vec_i, vec_j)
#            print(F"-- {dist_vec}, {taxi}")
            if taxi > maxi:
                maxi = taxi
    return maxi

with open("input", "r") as f:
    data = f.read().split("\n\n")
    
scans = [np.genfromtxt(StringIO(x), skip_header=1, delimiter=",") for x in data]

# assuming we are looking in +x direction, our hair going +1, ears +-z,
# generate matrices that turn everywhere else
rotmats = [np.array([[ 1, 0, 0],
            [ 0, 1, 0], #identity
            [ 0, 0, 1]])]

for i in range(3):
    rotmats.append(rotate(rotmats[0], 0, i+1)) # 4mal +x
    
rotmats.append(rotate(rotmats[0], 1, 2)) # -x
for i in range(3):
    rotmats.append(rotate(rotmats[4], 0, i+1)) # 4mal -x

rotmats.append(rotate(rotmats[0], 2, 1)) # +y
for i in range(3):
    rotmats.append(rotate(rotmats[8], 1, i+1)) # 4mal +y
    
rotmats.append(rotate(rotmats[8], 2, 2)) # -y
for i in range(3):
    rotmats.append(rotate(rotmats[12], 1, i+1)) # 4mal -y

rotmats.append(rotate(rotmats[0], 1, 1)) # +z
for i in range(3):
    rotmats.append(rotate(rotmats[16], 2, i+1)) # 4mal +z

rotmats.append(rotate(rotmats[16], 1, 2)) # -z
for i in range(3):
    rotmats.append(rotate(rotmats[20], 2, i+1)) # 4mal -z
# all rotations done!

matches = []
for scann in scans:
    match = []
    # for scan in scans:
    for scan in scans:
        a = orientate(scann, scan)
        match.append(a)
        # print()
    matches.append(match)

for i in matches:
    a = []
    for k, j in enumerate(i):
#        print(j, end=" ")
        if str(j).isdigit():
            a.append(k)
#    print()

chains = build_chains(matches)
scans_oriented = unwonkyfy(scans, chains, matches, rotmats)
scans_overlapped, total_movement = overlap(scans_oriented, chains)
scan_unique = np.unique(np.concatenate(scans_overlapped),axis=0)

print(F"Finally! There are {scan_unique.shape[0]} beacons in this godforsaken ditch.")

max_dist = find_max_distance(total_movement)

print(F"The maximum Taxicab-distance between any two scanners is {max_dist}.")
    
print()
print("--- %s seconds ---" % (time.time() - start_time))














