import numpy as np
import time
start_time = time.time()

fishies = np.genfromtxt("input", delimiter=",", dtype="int")

for day in range(80):
    for i in range(len(fishies)):
        if fishies[i] == 0:
            fishies[i] = 6
            fishies = np.append(fishies, 8)
        else:
            fishies[i] -= 1
            
print(F"Number of Fishies: {len(fishies)}")
print("--- %s seconds ---" % (time.time() - start_time))

#testfile: 
#Number of Fishies: 5934
#--- 0.06827664375305176 seconds ---

#real input
#Number of Fishies: 359344
#--- 48.101457357406616 seconds ---