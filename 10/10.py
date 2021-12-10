import time
start_time = time.time()

# chunk markers: () [] {} <>

def score(line):
    error = 0
    print(line)
    while (len(line) > 0 and error == 0 and not all(x in pair for x in line)):
        error, line = resolve(line)
        print(line)
    return error, line

def resolve(sub):
    if len(sub) > 1:
        if sub[0] in pair:
            if sub[1] in pair:
                err, subn = resolve(sub[1:])
                sub = sub[0]+subn
                if len(sub) == 1:
                    return 0, sub
                if err > 0:
                    return err, sub
            if sub[1] == pair[sub[0]]:
                return 0, sub[2:]
            elif sub[1] in [y for x,y in pair.items()]:
                return scoredict[sub[1]], sub
        else:
            return 1, sub
        return 0, sub
    return 0, ""

error_score = 0
nav = []
num_lines = 0

pair = {"(": ")",
        "[": "]",
        "{": "}",
        "<": ">"}

scoredict = {")": 3,
             "]": 57,
             "}": 1197,
             ">": 25137}
    
with open("input", "r") as f:
    for line in f.read().splitlines(): #splitlines sonst newline am ende!
        print(F"-----------")
        num_lines += 1
        n, rest = score(line)
        if n > 0:
            error_score += n
        else:
            nav.append([line,rest])

print(F"{len(nav)}/{num_lines} lines were not corrupted.")
print(F"Error score of corrupted lines: {error_score}")

comp_score = []
ind_score = {"(": 1,
             "[": 2,
             "{": 3,
             "<": 4}

for row in nav:
    sco = 0
    for brack in reversed(row[1]):
        sco = sco * 5 + ind_score[brack]
    comp_score.append(sco)

comp_score.sort()
print(F"Middle score of all completion scores: {comp_score[round(len(comp_score)/2)-1]}")

print()
print("--- %s seconds ---" % (time.time() - start_time))
