import time
start_time = time.time()

from copy import deepcopy
import numpy as np
from collections import Counter

class pawn:
    def __init__(self, position, score = None):
        self.position = position
        if score is None:
            self.score = 0
    
    def move(self, dist):
        self.position = (self.position + dist -1)%10 +1
        self.score += self.position
            
        return self.position, self.score

class det_die:
    def __init__(self):
        self.cycle = 0
    
    def roll(self,amount = 1):
        out = 0
        for i in range(amount):
            self.cycle = self.cycle % 100 + 1
            out += self.cycle
        return out

class dirac_die:
    def __init__(self):
        self.cycle = 0
        self.rolls = []
        for i in [1,2,3]:
            for j in [1,2,3]:
                for k in [1,2,3]:
                    self.rolls.append(i+j+k)
        self.rolls = list(Counter(self.rolls).items())
    
    def roll(self,amount = 3):
        if amount != 3:
            return "???"
        return self.rolls

def mwi_game(p_one, p_two, dice, active_player, multiplier=1):
    result = np.array([0,0])
    # print(p_one.score, p_two.score)
    if p_one.score >= 21:
        result += np.array([1,0]) * multiplier
        # print(F"       STOOOP!         {result}")
    elif p_two.score >= 21:
        result += np.array([0,1]) * multiplier
        # print(F"               STOOOP! {result}")
    else:
        for roll in die.roll():
            if active_player == 1:
                p = deepcopy(p_one)
                p.move(roll[0])
                result += mwi_game(p, p_two, dice, 2, multiplier*roll[1])
            elif active_player == 2:
                p = deepcopy(p_two)
                p.move(roll[0])
                result += mwi_game(p_one, p, dice, 1, multiplier*roll[1])
    return result

# Player 1 starting position: 10
# Player 2 starting position: 4
p1_start = 10
p2_start =  4

# part 1
p1 = pawn(p1_start)
p2 = pawn(p2_start)
die = det_die()

turn = 0
while True:
    turn += 1
    if turn % 2 == 1:
        p = p1
    else:
        p = p2
    p.move(die.roll(3))
    if p.score >= 1000:
        break

print(F"Game endet after {turn} moves. Scores:")
print(F"Player 1: {p1.score}     Player 2: {p2.score}")
print(F"Die rolls * losing score: {turn * 3 * min(p1.score, p2.score)}")

# part 2
p1 = pawn(p1_start)
p2 = pawn(p2_start)
die = dirac_die()

wow = mwi_game(p1, p2, die, 1)
print()
print(F"Multidimensional game endet {wow[0]} to {wow[1]} after {wow[0] + wow[1]} games.")

print()
print("--- %s seconds ---" % (time.time() - start_time))
