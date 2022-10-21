"""Advent of Code Day 23"""

import time
from queue import PriorityQueue

# test
# #############
# #...........#
# ###D#C#D#B###
#   #B#A#A#C#
#   #########

# actual
# #############
# #...........#
# ###D#C#D#B###
#   #B#A#A#C#
#   #########

class cave:
    def __init__(self, population: list):
        if not isinstance(population, list) or len(population) != 19:
            raise TypeError("Input must be list of length 19")
        
        # initialize cave with restrictions and population
        self.spots = [
            spot(location=0, neighbours=([1])),
            spot(location=1, neighbours=([0, 2])),
            spot(location=2, neighbours=([1, 3, 11]), allowed=[]),
            spot(location=3, neighbours=([2, 4])),
            spot(location=4, neighbours=([3, 5, 13]), allowed=[]),
            spot(location=5, neighbours=([4, 6])),
            spot(location=6, neighbours=([5, 7, 15]), allowed=[]),
            spot(location=7, neighbours=([6, 8])),
            spot(location=8, neighbours=([7, 9, 17]), allowed=[]),
            spot(location=9, neighbours=([8, 10])),
            spot(location=10, neighbours=([9])),
            spot(location=11, neighbours=([2, 12]), allowed=["A"]),
            spot(location=12, neighbours=([11]), allowed=["A"]),
            spot(location=13, neighbours=([4, 14]), allowed=["B"]),
            spot(location=14, neighbours=([13]), allowed=["B"]),
            spot(location=15, neighbours=([6, 16]), allowed=["C"]),
            spot(location=16, neighbours=([15]), allowed=["C"]),
            spot(location=17, neighbours=([8, 18]), allowed=["D"]),
            spot(location=18, neighbours=([17]), allowed=["D"]),
            ]
        for i, amph in enumerate(population):
            self.spots[i].amphipod = amph
        self.population = population
    
    def get_map(self) -> str:
        """output current situation in cave as ASCII graphic"""
        outstring = "▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒"
        for i in range(11):
            if self.spots[i].amphipod is None:
                outstring += "."
            else:
                outstring += self.spots[i].amphipod
        outstring += "▒\n▒▒"
        for i in range(11,18,2):
            outstring += "▒"
            if self.spots[i].amphipod is None:
                outstring += "."
            else:
                outstring += self.spots[i].amphipod
        outstring += "▒▒▒\n  "
        for i in range(12,19,2):
            outstring += "▒"
            if self.spots[i].amphipod is None:
                outstring += "."
            else:
                outstring += self.spots[i].amphipod
        outstring += "▒  \n  ▒▒▒▒▒▒▒▒▒  "
        return outstring
    
    def next_situations(self):
        """generate list of possible moves and return them with score and hash"""
        situations = {}
        for spot in [taken for taken in self.spots if not taken.is_empty()]:
            targets = self.acquire_targets(spot)
            for target in targets:
                situation = self.population.copy()
                situation[spot.location] = None
                situation[target] = spot.amphipod
                situations[tuple(situation)] = targets[target]
        # for sit in situations:
        #     print(situations[sit], sit)
        return situations

    def acquire_targets(self, spot):
        """find possible targets to move to from currrent location,
        return them with associated cost
        """
        def go_next(self, current_pos, visited=set(), reachable={}, steps=0):
            """recursively venture deeper into cave, noting where you could
            legally end up and how far it is"""
            visited.add(current_pos)
            if (spot.location != current_pos
                and self.is_allowed(self.spots[current_pos], spot.amphipod, spot.location)):
                reachable[current_pos] = steps
            for neighbour in self.spots[current_pos].neighbours:
                if neighbour not in visited:
                    if self.spots[neighbour].is_empty():
                        vis, reach = go_next(self, neighbour, visited, reachable, steps+1)
                        visited.update(vis)
                        reachable = reachable | reach
            return visited, reachable
        
        cost = {"A":1, "B":10, "C":100, "D":1000}
        _ , reachable = go_next(self, spot.location)
        for target in reachable:
            reachable[target] *= cost[spot.amphipod]
        return reachable
    
    def is_allowed(self, spot, new_amphipod, start_location):
        """Check if an amphipod may move here"""
        if new_amphipod not in spot.allowed:
            return False
        if start_location <= 10 and spot.location <= 10:
            return False
        if spot.location > 10:
            rooms = [[11, 12], [13, 14], [15, 16], [17,18]]
            room = [x for x in rooms if spot.location in x]
            for place in room[0]:
                if (self.spots[place].amphipod not in self.spots[place].allowed
                    and self.spots[place].amphipod is not None):
                    return False            
        return True

class spot:
    def __init__(self, amphipod=None, allowed=["A","B","C","D"],
                 location=None, neighbours=None):
        self.amphipod = amphipod
        self.allowed = allowed
        self.location = location
        self.neighbours = neighbours
    
    def is_empty(self):
        """Check if spot is taken"""
        if self.amphipod is not None:
            return False
        return True
    
# track time
start_time = time.time()

testpop = [None, None, None, None, None, None, None, None, None, None, None,
            "B", "A", "C", "D", "B", "C", "D", "A"]
# testpop = [None, None, None, None, None, None, None, None, None, None, None,
#            "D", "B", "C", "A", "D", "A", "B", "C"]

targetpop = [None, None, None, None, None, None, None, None, None, None, None,
           "A", "A", "B", "B", "C", "C", "D", "D"]

situations = {}
new_situations = PriorityQueue()
new_situations.put((0, 0, tuple(testpop)))
i = 0

while not new_situations.empty():
    current_energy, _, current_soi = new_situations.get()
    current_cave = cave(list(current_soi))
    next_situations = current_cave.next_situations()
    for next_situation in next_situations:
        if (next_situation not in situations or
            situations[next_situation] > next_situations[next_situation] + current_energy):
            situations[next_situation] = next_situations[next_situation] + current_energy
            i += 1
            new_situations.put((current_energy + next_situations[next_situation], i, next_situation))
    if tuple(targetpop) in situations:
        break

print(situations[tuple(targetpop)], targetpop)
print(f"Final configuration reached with {situations[tuple(targetpop)]} energy spent.")

print()
print(f"--- {time.time() - start_time} seconds ---")
