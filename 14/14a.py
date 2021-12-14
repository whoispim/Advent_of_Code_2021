import time
start_time = time.time()

from collections import Counter

with open("input", "r") as file:
    seq, rules_pre = file.read().split("\n\n")
    rules = dict(x.split(" -> ") for x in rules_pre[:-1].split("\n"))

for steps in range(10):
    # print(F"Step {steps+1}")
    for i in range(len(seq)-2, -1, -1):
        if seq[i:i+2] in rules:
            seq = "".join([seq[:i+1], rules[seq[i:i+2]], seq[i+1:]])

counts = Counter(seq)
score = counts[max(counts, key=counts.get)] \
        - counts[min(counts, key=counts.get)]
        
print(F"Polymer score after {steps+1} steps: {score}")

print()
print("--- %s seconds ---" % (time.time() - start_time))