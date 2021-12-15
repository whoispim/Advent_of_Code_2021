import time
start_time = time.time()

import numpy as np
import networkx as nx
from queue import PriorityQueue

cavern = np.genfromtxt("input", delimiter=1, dtype=int)

G = nx.grid_2d_graph(cavern.shape[0], cavern.shape[1])
for row, col in np.ndindex(cavern.shape):
    G.nodes[row,col]["weight"] = cavern[row,col]

# Dijkstar copied/learned from Red Blob Games
frontier = PriorityQueue()
frontier.put((0,0), 0)
came_from = dict()
cost_so_far = dict()
came_from[(0,0)] = None
cost_so_far[(0,0)] = 0
goal = (cavern.shape[0]-1, cavern.shape[1]-1)

while not frontier.empty():
   current = frontier.get()

   if current == goal:
      break
   
   for next in G.neighbors(current):
      new_cost = cost_so_far[current] + G.nodes[next]["weight"]
      if next not in cost_so_far or new_cost < cost_so_far[next]:
         cost_so_far[next] = new_cost
         priority = new_cost
         frontier.put(next, priority)
         came_from[next] = current

path = []
current = goal
while current != (0,0):
    path.append(current)
    current = came_from[current]
path.append((0,0))

for x in range(cavern.shape[0]):
    for y in range(cavern.shape[1]):
        if (x,y) in path:
            print(G.nodes[(x,y)]["weight"], end="")
        else:
            print(" ", end="")
    print()
    
print()
print(F"Total risk to get here: {cost_so_far[goal]}")

print()
print("--- %s seconds ---" % (time.time() - start_time))
