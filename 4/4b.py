# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

def check_boards(cards, mask, zahl):
    for i, card in enumerate(cards):
        for j, row in enumerate(card):
            for k, num in enumerate(row):
                if num == zahl:
                    mask[i][j][k] = True
    return mask

def didiwin(mask):
    for i, card in enumerate(mask):
        for j, row in enumerate(card):
            if row.all():
                return True, i
        for j, row in enumerate(card.transpose()):
            if row.all():
                return True, i
    return False, 0



draw = np.loadtxt("input", max_rows=1, delimiter=",")
data = np.genfromtxt("input", skip_header=2)

cards = np.array_split(data, data.shape[0]/5) #bingofelder separieren

hitmask = np.array_split(data==True, data.shape[0]/5) #bingofelder separieren

for i, zahl in enumerate(draw):
    print(F"Zahl Nr. {i}: {int(zahl)}")
    hitmask = check_boards(cards, hitmask, zahl)
    win = True
    while win: #while im mehrere sieger gleichzeitig zu kicken
        win, which = didiwin(hitmask)
        if win:
            print(F"Board Nr. {which} gewinnt... Weg damit.")
            if len(cards) > 1:
                cards.pop(which)
                hitmask.pop(which)
            else:
                break
    else:
        print(F"Übrig: {len(cards)}")
        continue #starte loop von vorn falls aus dem unterloop nicht gebreaked wurde
    break

print("Zuletzt gewinnt:")
print(cards[which])
print(hitmask[which])
#summe der nicht markierten via invertierter maske
sum_un = cards[which][np.invert(hitmask[which])].sum()
print(F"Summe der nicht markierten: {sum_un}")
print(F"Multipliziert mit Nr. {zahl}: {zahl*sum_un}")
