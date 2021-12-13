import time
start_time = time.time()

import numpy as np

f = "input"
dotcoords = np.genfromtxt(f, dtype="int",  delimiter=",", 
                          skip_footer=12 if f=="input" else 3)

folds = []
with open(f, "r") as file:
    lines = file.readlines()
    for line in lines[-12:] if f=="input" else lines[-2:]:
        a = line.split()[2].split("=")
        folds.append([0 if a[0]=="x" else 1, int(a[1])])

for fold in folds:
    for dot in dotcoords:
        if dot[fold[0]] > fold[1]:
            dot[fold[0]] = fold[1] * 2 - dot[fold[0]]
    dotcoords = np.unique(dotcoords, axis=0)
    # break # break for 13a

dotmatrix = np.zeros((max(dotcoords[:,1]+1), max(dotcoords[:,0])+1))
for dot in dotcoords:
    dotmatrix[dot[1],dot[0]] = 1

print()
for x in dotmatrix:
    for y in x:
        if y == 1:
            print("X", end="")
        else:
            print(" ", end="")
    print()

print()
print("--- %s seconds ---" % (time.time() - start_time))