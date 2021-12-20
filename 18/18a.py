import time
start_time = time.time()

import math

def snail_add(num1, num2):
    num = "[" + num1 + "," + num2 + "]"
    num = reduce(num)
    return num

def reduce(num):
    cnum = num
    onum = ""
    while onum != num:
        onum = num
        num = explode(onum)
    onum = ""
    while onum != num:
        onum = num
        num = ssplit(onum)
    if cnum != num:
        reduce(num)
    return num
    
    # print(num)
    # layer = 0
    # danger = 0 # 1: explode; 2: split
    # for i in range(len(num)):
    #     if num[i] == "[":
    #         layer += 1
    #     elif num[i] == "]":
    #         layer -= 1
    #     print(" ", end="")
    #     if layer > 4: # danger!
    #         danger = 1
    #         for j in range(i+1, len(num)):
    #             if num[j] == "]": # grab until end of layer
    #                 break
    #         break
    #     if num[i:i+2].isdigit():
    #         danger = 2
    #         break
    # if danger == 1:
    #     a, b = map(int, num[i+1:j].split(","))
    #     print(a, b)
    #     num = num[:i] + "0" + num[j+1:]
    #     for h in range(i+2,len(num)): # go right
    #         if num[h].isdigit():
    #             if num[h+1].isdigit():
    #                 num = num[:h] + str(int(num[h:h+2]) + b) + num[h+2:]
    #             else:
    #                 num = num[:h] + str(int(num[h]) + b) + num[h+1:]
    #             break
    #     for h in range(i-1, -1, -1): # go left
    #         if num[h].isdigit():
    #             num = num[:h] + str(int(num[h]) + a) + num[h+1:]
    #             break
    # elif danger == 2:
    #     a = str(math.floor(int(num[i:i+2]) / 2))
    #     b = str(math.ceil(int(num[i:i+2]) / 2))
    #     print(num[i:i+2])
    #     num = num[:i] + "[" + a + "," + b + "]" + num[i+2:]
    # # print()
    # if danger != 0:
    #     num = reduce(num)
    # return num

def explode(num):
    print(num)
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
    if danger == 1:
        a, b = map(int, num[i+1:j].split(","))
        # print(a, b)
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
                num = num[:h] + str(int(num[h]) + a) + num[h+1:]
                break
    return num

def ssplit(num):
    print(num)
    danger = 0 # 1: explode; 2: split
    for i in range(len(num)):
        if num[i:i+2].isdigit():
            danger = 2
            break
    if danger == 2:
        a = str(math.floor(int(num[i:i+2]) / 2))
        b = str(math.ceil(int(num[i:i+2]) / 2))
        # print(num[i:i+2])
        num = num[:i] + "[" + a + "," + b + "]" + num[i+2:]    
    return num

# snail_num = "[[[[4,3],4],4],[7,[[8,4],9]]]"
snail_num = "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]"
snail_todo = ["[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
"[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
"[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
"[7,[5,[[3,8],[1,4]]]]",
"[[2,[2,2]],[8,[8,1]]]",
"[2,9]",
"[1,[[[9,3],9],[[9,0],[0,7]]]]",
"[[[5,[7,4]],7],1]",
"[[[[4,2],2],6],[8,7]]"]
for todo in snail_todo:
    snail_num = snail_add(snail_num, todo)
    print()
    print(snail_num)
    break
print("[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]")

    
print()
print("--- %s seconds ---" % (time.time() - start_time))














