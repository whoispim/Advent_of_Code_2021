import time
start_time = time.time()

import math

class probe:
    def __init__(self, vel, path = None):
        self.vel = vel
        if path is None:
            self.path = [[0,0]]
        
    def pos(self):
        global target_area
        status = 0 # status 1: hit; status 2: missed
        if (target_area[0][0] <= self.path[-1][0] <= target_area[1][0] and 
            target_area[0][1] <= self.path[-1][1] <= target_area[1][1]):
            status = 1
        if (self.path[-1][0] > target_area[1][0] or 
            self.path[-1][1] < target_area[0][1]):
            status = 2
        return self.path[-1], status
    
    def travel(self):
        new_x = self.path[-1][0] + self.vel[0]
        new_y = self.path[-1][1] + self.vel[1]
        if self.vel[0] > 0: self.vel[0] -= 1
        if self.vel[0] < 0: self.vel[0] += 1
        self.vel[1] -= 1
        self.path.append([new_x, new_y])

target_area = [[156,-110],
               [202, -69]]

# test area
# target_area = [[20,-10],
#               [30, -5]]

vel_min = [math.ceil((math.sqrt(target_area[0][0]*8+1)-1)/2),
           target_area[0][1]]
vel_max = [target_area[1][0],
           -target_area[0][1]-1]

# part 1
p = probe([vel_min[0],vel_max[1]])
while p.pos()[1] == 0:
    p.travel()

print("Maximum height reached while still hitting target:",max(y[1] for y in p.path))
print()

# part 2
hitting_velocities = []
for vel_y in range(vel_max[1], vel_min[1] - 1, -1):
    for vel_x in range(vel_min[0], vel_max[0] + 1):
        p = probe([vel_x,vel_y])
        while p.pos()[1] == 0:
            p.travel()
        if p.pos()[1] == 1:
            print("X", end="")
            hitting_velocities.append([vel_x, vel_y])
        else:
            if vel_y == 0: print("—", end="")
            else: print("·", end="")
    print("")

print()
print(F"There are {len(hitting_velocities)} different ways to hit the target area.")

print()
print("--- %s seconds ---" % (time.time() - start_time))














