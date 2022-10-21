import time


def push_it(var_n: int):
    def change(var_w, var_z):
        ret_z = var_z * 26 + var_n + var_w
        return True, ret_z
    return change


def pull_it(var_m: int):
    def change(var_w, var_z):
        if var_z % 26 + var_m == var_w:
            ret_z = var_z / 26
            return True, int(ret_z)
        return False, var_z
    return change


# track time
start_time = time.time()

instructions = []

with open("input", "r") as infile:
    lines = infile.read().split("\n")
    blocks = []
    for i in range(14):
        blocks.append(lines[i*18:(i+1)*18])
    for i, block in enumerate(blocks):
        if block[4][6:] == "1":
            n = int(block[15][6:])
            print(i, "-->push", n)
            instructions.append(push_it(n))
        else:
            m = int(block[5][6:])
            print(i, "<--pull", m)
            instructions.append(pull_it(m))

succ_dict = {"": 0}  # succ = success!
for j, inst in enumerate(instructions):
    new_succ = {}
    for mod_num, z in succ_dict.items():
        for i in range(1, 10):
            succ, new_z = inst(i, z)
            if succ:
                new_succ[mod_num+str(i)] = new_z
    succ_dict = new_succ.copy()
    print(f"{j}, Valid candidates: {len(succ_dict)}")

sorted_model_numbers = sorted(succ_dict.keys())
print(f"Highest valid model number: {sorted_model_numbers[-1]}")
print(f"Lowest valid model number:  {sorted_model_numbers[0]}")

print()
print(f"--- {time.time() - start_time} seconds ---")
