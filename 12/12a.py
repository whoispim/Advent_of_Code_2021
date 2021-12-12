import time
start_time = time.time()

def move(path):
    if path[-1] == "end":
        print(path)
        global paths
        paths.append(path)
    else:
        for next in cavecons[path[-1]]:
            if next.isupper() or next not in path:
                move(path + [next])
                
conlist = []
with open("input", "r") as f:
    for line in f.read().splitlines():
        conlist.append(line.split("-"))

flatcon = []
for sub in conlist:
    for item in sub:
        flatcon.append(item)

cavecons = {}
for cave in set(flatcon):
    templist = []
    for con in conlist:
        if cave in con:
            templist.append([x for x in con if x!=cave][0])
    cavecons[cave] = templist
        
paths = []

move(["start"])

print(F"There are {len(paths)} paths through this cave system that don't visit small caves more than once!")

print()
print("--- %s seconds ---" % (time.time() - start_time))