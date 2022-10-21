import time
import numpy as np

# track time
start_time = time.time()


def move_east(sfloor):
    valid_moves = np.zeros(sfloor.shape)
    newfloor = sfloor.copy()
    for i in range(sfloor.shape[0]):
        for j in range(sfloor.shape[1]):
            if (sfloor[i, j] == 1
                    and sfloor[i, (j+1) % sfloor.shape[1]] == 0):
                valid_moves[i, j] = 1

    for i in range(sfloor.shape[0]):
        for j in range(sfloor.shape[1]):
            if valid_moves[i, j] == 1:
                newfloor[i, j] = 0
                newfloor[i, (j+1) % sfloor.shape[1]] = 1
    return newfloor


def move_south(sfloor):
    valid_moves = np.zeros(sfloor.shape)
    newfloor = sfloor.copy()
    for i in range(sfloor.shape[0]):
        for j in range(sfloor.shape[1]):
            if (sfloor[i, j] == 2
                    and sfloor[(i+1) % sfloor.shape[0], j] == 0):
                valid_moves[i, j] = 1

    for i in range(sfloor.shape[0]):
        for j in range(sfloor.shape[1]):
            if valid_moves[i, j] == 1:
                newfloor[i, j] = 0
                newfloor[(i+1) % sfloor.shape[0], j] = 2
    return newfloor


with open("input", "r") as f:
    lines = f.read().split("\n")
x_len = len(lines)
y_len = len(lines[0])
seafloor = np.zeros((x_len, y_len))
for i, line in enumerate(lines):
    for j, spot in enumerate(line):
        if spot == ">":
            seafloor[i, j] = 1
        elif spot == "v":
            seafloor[i, j] = 2

steps = 0
while True:
    steps += 1
    new_seafloor = move_east(seafloor)
    new_seafloor = move_south(new_seafloor)
    if np.array_equal(new_seafloor, seafloor):
        break
    seafloor = new_seafloor

print_dict = {0: ".", 1: ">", 2: "v"}
for i in seafloor:
    outstr = ""
    for j in i:
        outstr += print_dict[j]
    print(outstr)

print(f"No further movement after {steps} steps.")


print()
print(f"--- {time.time() - start_time} seconds ---")
