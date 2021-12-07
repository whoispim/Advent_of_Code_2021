import time
start_time = time.time()

with open("input","r") as f:
    crabs = [int(fish) for fish in f.readline().split(",")]

crab_pos=[]
for a in range(max(crabs)+1):
    crab_pos.append(crabs.count(a))

acc_dist = [0] * len(crab_pos)
for i, amount in enumerate(crab_pos):
    for j in range(len(crab_pos)):
        acc_dist[j] = acc_dist[j] + abs(j-i) * amount

print("Lowest fuel used:")
print(F"  {min(acc_dist)} units for position {acc_dist.index(min(acc_dist))}")
print()
print("--- %s seconds ---" % (time.time() - start_time))