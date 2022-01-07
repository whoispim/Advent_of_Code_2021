import time
start_time = time.time()

import networkx as nx
from queue import PriorityQueue

#############
#.. . . . ..# 11 empty but only 7 usable
###B#C#B#D###
  #A#D#C#A#
  #########

# state is recorded as top 7 spaces, then front row of burrow, then back

def populate(Graph, instring):
    newG = Graph.copy()
    newG.nodes["a1"]["pres"] = instring[7]
    newG.nodes["b1"]["pres"] = instring[8]
    newG.nodes["c1"]["pres"] = instring[9]
    newG.nodes["d1"]["pres"] = instring[10]
    newG.nodes["a2"]["pres"] = instring[11]
    newG.nodes["b2"]["pres"] = instring[12]
    newG.nodes["c2"]["pres"] = instring[13]
    newG.nodes["d2"]["pres"] = instring[14]
    return newG

G = nx.Graph()
G.add_nodes_from(["lo","li","ab","bc","cd","ri","ro",
                       "a1","a2","b1","b2","c1","c2","d1","d2"], pres = None)
G.add_edges_from([("lo","li",{"weight": 1}),
                  ("li","a1",{"weight": 2}),
                  ("li","ab",{"weight": 2}),
                  ("a1","a2",{"weight": 1}),
                  ("a1","ab",{"weight": 2}),
                  ("ab","b1",{"weight": 2}),
                  ("ab","bc",{"weight": 2}),
                  ("b1","b2",{"weight": 1}),
                  ("b1","bc",{"weight": 2}),
                  ("bc","c1",{"weight": 2}),
                  ("bc","cd",{"weight": 2}),
                  ("c1","c2",{"weight": 1}),
                  ("c1","cd",{"weight": 2}),
                  ("cd","d1",{"weight": 2}),
                  ("cd","ri",{"weight": 2}),
                  ("d1","d2",{"weight": 1}),
                  ("d1","ri",{"weight": 2}),
                  ("ri","ro",{"weight": 1})
                  ])

start = ".......BCBDADCA"
goal =  ".......ABCDABCD"

enerdict = {"A": 1,
            "B": 10,
            "C": 100,
            "D": 1000}

S = populate(G, start)

# now build a graph of graphs?

print()
print("--- %s seconds ---" % (time.time() - start_time))
