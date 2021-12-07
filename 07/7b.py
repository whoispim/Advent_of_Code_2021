import time
start_time = time.time()

with open("input","r") as f:
    crabs = [int(fish) for fish in f.readline().split(",")]

crab_pos=[]
for a in range(max(crabs)+1):
    crab_pos.append(crabs.count(a))

triangular = [0] * len(crab_pos) #precalculate fuel consumption for distance n
for i in range(1,len(triangular)):
    triangular[i] = triangular[i-1] + i

acc_dist = [0] * len(crab_pos)
for i, amount in enumerate(crab_pos):
    for j in range(len(crab_pos)):
            acc_dist[j] = acc_dist[j] + triangular[abs(i-j)] * amount

print("Lowest fuel used:")
print(F"  {min(acc_dist)} units for position {acc_dist.index(min(acc_dist))}")
print()
print("--- %s seconds ---" % (time.time() - start_time))