import time
start_time = time.time()

import math
import numbers

def snail_add(num1, num2):
    num = "[" + num1 + "," + num2 + "]"
    num = reduce(num)
    return num

def reduce(num):
    onum = ""
    while onum != num:
        onum = num
        num = explode(onum)
        if onum != num:
            continue
        num = ssplit(onum)
    return num

def explode(num):
    layer = 0
    danger = 0 # 1: explode; 2: split
    for i in range(len(num)):
        if num[i] == "[":
            layer += 1
        elif num[i] == "]":
            layer -= 1
        # print(" ", end="")
        if layer > 4: # danger!
            danger = 1
            for j in range(i+1, len(num)):
                if num[j] == "]": # grab until end of layer
                    break
            break
        
#    print(num, end="")
#    if danger != 0:
#        print(" explode")
#    else:
#        print()
        
    if danger == 1:
        a, b = map(int, num[i+1:j].split(","))
        num = num[:i] + "0" + num[j+1:]
        for h in range(i+2,len(num)): # go right
            if num[h].isdigit():
                if num[h+1].isdigit():
                    num = num[:h] + str(int(num[h:h+2]) + b) + num[h+2:]
                else:
                    num = num[:h] + str(int(num[h]) + b) + num[h+1:]
                break
        for h in range(i-1, -1, -1): # go left
            if num[h].isdigit():
                if num[h-1].isdigit():
                    num = num[:h-1] + str(int(num[h-1:h+1]) + a) + num[h+1:]
                else:
                    num = num[:h] + str(int(num[h]) + a) + num[h+1:]
                break
    return num

def ssplit(num):
    danger = 0 # 1: explode; 2: split
    for i in range(len(num)):
        if num[i:i+2].isdigit():
            danger = 2
            break
    
#    print(num, end="")
#    if danger != 0:
#        print(" split")
#    else:
#        print()
        
    if danger == 2:
        a = str(math.floor(int(num[i:i+2]) / 2))
        b = str(math.ceil(int(num[i:i+2]) / 2))
        num = num[:i] + "[" + a + "," + b + "]" + num[i+2:]    
    return num

def get_magnitude(num):
    numlist = eval(num)
    magni = deepmag(numlist)
    return magni

def deepmag(numlist):
    ab = [0,0]
    for i, partner in enumerate(numlist):
        if isinstance(partner, numbers.Number):
            ab[i] = partner
        else:
            ab[i] = deepmag(partner)
    return 3*ab[0] + 2*ab[1]
            
with open("input", "r") as f:
    snail = f.read().split("\n")    

snail_num = snail[0]
snail_todo = snail[1:]

for todo in snail_todo:
    snail_num = snail_add(snail_num, todo)
#    print()
#    print(snail_num)

magnitude = get_magnitude(snail_num)

print(F"The magnitude of this little snails math homework is {magnitude}.")

two_sum_magnitudes = []
for num1 in snail:
    for num2 in snail:
        if num1!=num2:
            two_sum_magnitudes.append(
                    get_magnitude(
                            snail_add(num1, num2)
                            )
                    )

print(F"The largest magnitude a snail can get by adding two different numbers is {max(two_sum_magnitudes)}.")

print()
print("--- %s seconds ---" % (time.time() - start_time))