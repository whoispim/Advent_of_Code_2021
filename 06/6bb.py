import time
start_time = time.time()

with open("input","r") as f:
    fishies = [int(fish) for fish in f.readline().split(",")]

fishbucket=[]
for a in range(9):
    fishbucket.append(fishies.count(a))

for day in range(256):
    fishbucket = fishbucket[1:7]\
        + [fishbucket[0]+fishbucket[7]]\
        + [fishbucket[8]]\
        + [fishbucket[0]]
    
print("Done in %s seconds" % (time.time() - start_time))
print(F"Number of Fishies: {sum(fishbucket)}")
