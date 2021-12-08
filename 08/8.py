#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

import time
start_time = time.time()

def reorder_segments(jumble):
    order = [""] * 7
    one = list([x for x in jumble if len(x)==2][0])
    sev = list([x for x in jumble if len(x)==3][0])
    fou = list([x for x in jumble if len(x)==4][0])
        
    order[0], *_ = set(sev)-set(one)
    order[3] = [x for x in fou if all(x in y for y in jumble if len(y)==5)][0]
    order[1], *_ = set(fou) - (set([x for x in order if x>""]) | set(one))
    l5a, l5b, l5c = [set(x) for x in jumble if len(x)==5]
    l6a, l6b, l6c = [set(x) for x in jumble if len(x)==6]
    order[6], *_ = l5a & l5b & l5c & l6a & l6b & l6c - set([x for x in order if x>""])
    order[4], *_ = set([x for x in jumble if len(x)==7][0]) - set(one) - set([x for x in order if x>""])
    order[2], *_ = (set(one) - l6a) | (set(one) - l6b) | (set(one) - l6c)
    order[5], *_ = set([x for x in jumble if len(x)==7][0]) - set([x for x in order if x>""])
    return "".join(order)

def decoder(jumble, cipher):
    output = []
    for x in jumble:
        temp = []
        for y in range(len(cipher)):
            if cipher[y] in x:
                temp.append("1")
            else:
                temp.append("0")
        output.append(seg_to_num("".join(temp)))
    return output

def seg_to_num(state):
    if state ==   "1110111":
        return 0
    elif state == "0010010":
        return 1
    elif state == "1011101":
        return 2
    elif state == "1011011":
        return 3
    elif state == "0111010":
        return 4
    elif state == "1101011":
        return 5
    elif state == "1101111":
        return 6
    elif state == "1010010":
        return 7
    elif state == "1111111":
        return 8
    elif state == "1111011":
        return 9
    else:
        return -1

code   = []
decode = []
with open("input","r") as f:
    for line in f.readlines():
        cod, decod = line.split(" | ")
        code.append(cod.split())
        decode.append(decod.split())

seg_order = []
for line in code:
    seg_order.append(reorder_segments(line))
result = []
for line, order in zip(decode, seg_order):
    result.append(decoder(line,order))

endea = 0
for wow in [1,4,7,8]:
    endea += sum(x.count(wow) for x in result)
    
endeb = sum([int("".join(map(str,x))) for x in result])

print(F"8a: Anzahl 1er, 4er, 7er und 8er: {endea}")
print(F"8b: Summer aller Ergebnisse:      {endeb}")

print()
print("--- %s seconds ---" % (time.time() - start_time))
