"""Advent of Code Day 24"""

import time

# track time
start_time = time.time()


def add(slot1: str, slot2: int | str):
    slot1 = slot_dict[slot1]
    if type(slot2) == str:
        slot2 = slot_dict[slot2]
        def change():
            ALU[slot1] += ALU[slot2]
        return change
    def change():
        ALU[slot1] += slot2
    return change

def mul(slot1: str, slot2: int | str):
    slot1 = slot_dict[slot1]
    if type(slot2) == str:
        slot2 = slot_dict[slot2]
        def change():
            ALU[slot1] *= ALU[slot2]
        return change
    def change():
        ALU[slot1] *= slot2
    return change

def eql(slot1: str, slot2: int | str):
    slot1 = slot_dict[slot1]
    if type(slot2) == str:
        slot2 = slot_dict[slot2]
        def change():
            if ALU[slot1] == ALU[slot2]:
                ALU[slot1] = 1
            else:
                ALU[slot1] = 0
        return change
    def change():
        if ALU[slot1] == slot2:
            ALU[slot1] = 1
        else:
            ALU[slot1] = 0
    return change

def div(slot: str, num: int):
    slot = slot_dict[slot]
    def change():
        ALU[slot] //= num
    return change

def mod(slot: str, num: int):
    slot = slot_dict[slot]
    def change():
        ALU[slot] = ALU[slot] % num
    return change

def inp(slot: str, input_num: int):
    real_slot = slot_dict[slot]
    def change():
        ALU[real_slot] = model_number // 10**(13-input_num) % 10
    return change

slot_dict = {"w": 0, "x": 1, "y": 2, "z": 3}

instructions = []
inp_count = 0
with open("input","r") as infile:
    for line in infile.read().split("\n"):
        try:
            int(line[6:])
        except ValueError:
            line = line[:6] + "'" + line[6:] + "'"
        if "inp" in line:
            instructions.append(eval(
                line[:3] + "('" + line[4] + "', " + str(inp_count) + ")"
            ))
            inp_count += 1
        else:
            instructions.append(eval(
                line[:3] + "('" + line[4] + "', " + line[6:] + ")"
            ))

# model_number = 100000000000000
model_number = 99999111111111
ALU = [0, 0, 0, 1]

# while ALU[3] != 0:
model_number -= 1
# while "0" in str(model_number): # skip zeros?
#     model_number -= 1
#     print(model_number)
ALU = [0, 0, 0, 0]
for i, inst in enumerate(instructions[:18*5]):
    inst()
    if i%18 == 0:
        print("---------")
    print(ALU)
if model_number%100000 == 0:
    print(f"{model_number} after {int(time.time() - start_time):4d} seconds")

print()
print(f"--- {time.time() - start_time} seconds ---")
