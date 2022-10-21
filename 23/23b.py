"""Advent of Code Day 23"""

import time
from queue import PriorityQueue

# test
#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

# actual
#############
#...........#
###D#C#D#B###
  #D#C#B#A#
  #D#B#A#C#
  #B#A#A#C#
  #########

class cave:
    def __init__(self, population: list):
        if not isinstance(population, list) or len(population) != 27:
            raise TypeError("Input must be list of length 27")

        # initialize cave with restrictions and population
        self.spots = [
            spot(location=0, neighbours=([1])),
            spot(location=1, neighbours=([0, 2])),
            spot(location=2, neighbours=([1, 3, 11]), allowed=[]),
            spot(location=3, neighbours=([2, 4])),
            spot(location=4, neighbours=([3, 5, 15]), allowed=[]),
            spot(location=5, neighbours=([4, 6])),
            spot(location=6, neighbours=([5, 7, 19]), allowed=[]),
            spot(location=7, neighbours=([6, 8])),
            spot(location=8, neighbours=([7, 9, 23]), allowed=[]),
            spot(location=9, neighbours=([8, 10])),
            spot(location=10, neighbours=([9])),
            spot(location=11, neighbours=([2, 12]), is_room=True, allowed=["A"]),
            spot(location=12, neighbours=([11, 13]), is_room=True, allowed=["A"]),
            spot(location=13, neighbours=([12, 14]), is_room=True, allowed=["A"]),
            spot(location=14, neighbours=([13]), is_room=True, allowed=["A"]),
            spot(location=15, neighbours=([4, 16]), is_room=True, allowed=["B"]),
            spot(location=16, neighbours=([15, 17]), is_room=True, allowed=["B"]),
            spot(location=17, neighbours=([16, 18]), is_room=True, allowed=["B"]),
            spot(location=18, neighbours=([17]), is_room=True, allowed=["B"]),
            spot(location=19, neighbours=([6, 20]), is_room=True, allowed=["C"]),
            spot(location=20, neighbours=([19, 21]), is_room=True, allowed=["C"]),
            spot(location=21, neighbours=([20, 22]), is_room=True, allowed=["C"]),
            spot(location=22, neighbours=([21]), is_room=True, allowed=["C"]),
            spot(location=23, neighbours=([8, 24]), is_room=True, allowed=["D"]),
            spot(location=24, neighbours=([23, 25]), is_room=True, allowed=["D"]),
            spot(location=25, neighbours=([24, 26]), is_room=True, allowed=["D"]),
            spot(location=26, neighbours=([25]), is_room=True, allowed=["D"]),
            ]
        for i, amph in enumerate(population):
            self.spots[i].amphipod = amph
        self.population = population

    def get_map(self) -> str:
        """output current situation in cave as ASCII graphic"""
        outstring = ""
        for i in range(11):
            if self.spots[i].amphipod is None:
                outstring += "."
            else:
                outstring += self.spots[i].amphipod
        for j in range(11,15):
            outstring += "\n "
            for i in range(j,j+13,4):
                outstring += " "
                if self.spots[i].amphipod is None:
                    outstring += "."
                else:
                    outstring += self.spots[i].amphipod
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
            rooms = [[11, 12, 13, 14],
                     [15, 16, 17, 18],
                     [19, 20, 21, 22],
                     [23, 24, 25, 26]]
            room = [x for x in rooms if spot.location in x]
            for place in room[0]:
                if (self.spots[place].amphipod not in self.spots[place].allowed
                    and self.spots[place].amphipod is not None):
                    return False
        return True
class spot:
    def __init__(self, amphipod=None, allowed=["A","B","C","D"], is_room=False,
                 location=None, neighbours=None):
        self.amphipod = amphipod
        self.allowed = allowed
        self.is_room = is_room
        self.location = location
        self.neighbours = neighbours

    def is_empty(self):
        """Check if spot is taken"""
        if self.amphipod is not None:
            return False
        return True


# track time
start_time = time.time()

# testpop = [None, None, None, None, None, None, None, None, None, None, None,
#             "B", "D", "D", "A",
#             "C", "C", "B", "D",
#             "B", "B", "A", "C",
#             "D", "A", "C", "A"]
testpop = [None, None, None, None, None, None, None, None, None, None, None,
            "D", "D", "D", "B",
            "C", "C", "B", "A",
            "D", "B", "A", "A",
            "B", "A", "C", "C"]

targetpop = [None, None, None, None, None, None, None, None, None, None, None,
           "A", "A", "A", "A",
           "B", "B", "B", "B",
           "C", "C", "C", "C",
           "D", "D", "D", "D"]

a = spot("A")
b = spot(allowed = ["B"])
c = cave(testpop)

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
            if i%100000 == 0:
                print(f"Energy: {current_energy:7d},    Situations: {len(situations):8d}   @ {int(time.time() - start_time):4d} seconds")
    if tuple(targetpop) in situations:
        break

print(situations[tuple(targetpop)], targetpop)
print(f"Final configuration reached with {situations[tuple(targetpop)]} energy spent.")

print()
print(f"--- {time.time() - start_time} seconds ---")
