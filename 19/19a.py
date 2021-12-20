import time
start_time = time.time()

import numpy as np
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
        print(j, end=" ")
        if str(j).isdigit():
            a.append(k)
    print()

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
        print(connected)
        
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
    overlist = []
    while len(overlapped) < 40:
        for i in list(set(range(40)) - set(overlist)):
            distlist = []
            buddy = connected[i]
            for j in range(sca[0].shape[0]):
                for k in range(sca[buddy].shape[0]):
                    distlist.append(np.subtract(sca[0][j],sca[buddy][k]))
            dist = Counter(distlist).most_common(1)[0][0]
            overlist.append(i)
            print(dist,i)

chains = build_chains(matches)
scans_oriented = unwonkyfy(scans, chains, matches, rotmats)
scans_overlapped = overlap(scans_oriented, chains)

print()
print("--- %s seconds ---" % (time.time() - start_time))














