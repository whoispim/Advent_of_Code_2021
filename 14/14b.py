import time
start_time = time.time()

with open("input", "r") as file:
    seq, rules_pre = file.read().split("\n\n")
    rules = dict(x.split(" -> ") for x in rules_pre[:-1].split("\n"))

# initiate counter
counts = {}
for letter in set("".join("".join(x) for x in list(rules.items()))):
    counts[letter] = 0
for letter in seq:
    counts[letter] += 1

seqbuck = {} # it's lanternfish all the way down to the bottom..
for i in range(len(seq)-1):
    pair = seq[i:i+2]
    if pair in seqbuck:
        seqbuck[pair] += 1
    else:
        seqbuck[pair] = 1

for steps in range(40):
    for bucket, amount in list(seqbuck.items()):
        if bucket in rules:
            seqbuck[bucket] -= amount
            subs = [bucket[0] + rules[bucket],
                    rules[bucket] + bucket[1]]
            for sub in subs:
                if sub in seqbuck:
                    seqbuck[sub] += amount
                else:
                    seqbuck[sub] = amount
            counts[rules[bucket]] += amount


score = counts[max(counts, key=counts.get)] \
        - counts[min(counts, key=counts.get)]
        
print(F"Polymer score after {steps+1} steps: {score}")

print()
print("--- %s seconds ---" % (time.time() - start_time))