import time
start_time = time.time()

import matplotlib.pyplot as plt
import math

# example: target area: x=20..30, y=-10..-5
# actual:  target area: x=156..202, y=-110..-69

def travel(xy, vel):
    xy[0] += vel[0]
    xy[1] += vel[1]
    if vel[0] > 0: vel[0] -= 1
    if vel[0] < 0: vel[0] += 1
    vel[1] -= 1
    return xy, vel

def hit(xy):
    if (target_area[0][0] <= coord[0] <= target_area[1][0] and 
        target_area[0][1] <= coord[1] <= target_area[1][1]):
        return True
    return False

def out(xy):
    if (xy[0] <= target_area[1][0] and 
        xy[1] >= target_area[1][1]):
        return False
    return True

def plot_target():
    areax = (target_area[0][0], target_area[0][0],
             target_area[1][0], target_area[1][0])
    areay = (target_area[0][1], target_area[1][1],
             target_area[1][1], target_area[0][1])
    plt.fill(areax, areay, color="#fff6eb")

target_area = [[156,-110],
               [202, -69]]

#target_area = [[20,-10],
#               [30, -5]]

# exclude values due to drag and gravity
lowest_x = math.ceil((math.sqrt(target_area[0][0]*8+1)-1)/2)
lowest_y = target_area[1][1]
highest_x = target_area[1][0]

#plot_target()
y_vel = lowest_y
success = False
past_success = False
y_record1 = 0
y_record2 = 0
for i in range(lowest_y,lowest_y+1000): # idk just brute force it..
    coord = [0,0]
    velo = [lowest_x,y_vel]
    path = [[0,0]]
    
    while True: # run until you missed..
        coord, velo = travel(coord, velo)
#        print(coord)
#        print(path)
        path.append(coord[:])
        if coord[1] > y_record1:
            y_record1 = coord[1]
        if hit(coord):
            success = True
            past_success = True
            y_record2 = y_record1
            print("X", end="")
            break
        if out(coord):
            success = False
            print(".", end="")
            break
    
#    plt.plot([x[0] for x in path], [y[1] for y in path])
#    plt.plot([x[0] for x in path], [y[1] for y in path], "o")
#    if past_success and not success:
#        y_vel -= 1
#        break
    y_vel += 1
    
print()
print(F"A maximum height of {y_record2} was reached",
      "while still hitting the target area.")

print()
print("--- %s seconds ---" % (time.time() - start_time))
