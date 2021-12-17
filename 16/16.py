import time
start_time = time.time()

from bitstring import BitStream
import numpy as np

# Examples
#in_hex = "D2FE28"
#in_hex = "8A004A801A8002F478"
#in_hex = "620080001611562C8802118E34"
#in_hex = "C0015000016115A2E0802F182340"
#in_hex = "A0016C880162017C3686B18A3D4780"

#in_hex = "C200B40A82" # finds the sum of 1 and 2, resulting in the value 3.
#in_hex = "04005AC33890" # finds the product of 6 and 9, resulting in the value 54.
#in_hex = "880086C3E88112" # finds the minimum of 7, 8, and 9, resulting in the value 7.
#in_hex = "CE00C43D881120" # finds the maximum of 7, 8, and 9, resulting in the value 9.
#in_hex = "D8005AC2A8F0" # produces 1, because 5 is less than 15.
#in_hex = "F600BC2D8F" # produces 0, because 5 is not greater than 15.
#in_hex = "9C005AC2F8F0" # produces 0, because 5 is not equal to 15.
#in_hex = "9C0141080250320F1802104A08" # produces 1, because 1 + 3 = 2 * 2.

# header
#   3 bit version
#   3 bit type
#      -ID==4: literal value
#       x*5 bits. leading 1 in all but last pack
#      -ID!=4: operator
#       next bit 0: 15 bits -> number -> bit-length of sub packets
#       next bit 1: 11 bits -> number of sub packets

def vers_type(instream):
    a_version = instream.read(3).uint
    a_type = instream.read(3).uint
    global ver_total
    ver_total += a_version
    return a_version, a_type

def read_literal(instream):
    outstream = BitStream()
    last = False
    while True:
        if not instream.read(1):
            last = True
        outstream.append(instream.read(4))
        if last:
            break
    return outstream

opdict = {0: "Sum",
          1: "Product",
          2: "Minimum",
          3: "Maximim",
          5: "Greater than",
          6: "Less than",
          7: "Equal to",}

def operate(instreams, opID, layer):
    print(F"{s*layer}OPERATION! {opdict[opID]} on {[x.bin for x in instreams]}")
    outstream = BitStream()
    val = []
    for i in instreams:
        val.append(i.uint)
    print(F"{s*layer}- Values: {val}")
    if opID == 0: # sum
        outstream.append(
                BitStream(hex=hex(sum(val)))
                )
    elif opID == 1: # product
        outstream.append(
                BitStream(hex=hex(np.prod(val)))
                )
    elif opID == 2: # minimum
        outstream.append(
                BitStream(hex=hex(min(val)))
                )
        
    elif opID == 3: # maximum
        outstream.append(
                BitStream(hex=hex(max(val)))
                )
    elif opID == 5: # greater than (first: 1, else: 0)
        if val[0] > val[1]:
            outstream.append(
                    BitStream(hex=hex(1))
                    )
        else:
            outstream.append(
                    BitStream(hex=hex(0))
                    )        
    elif opID == 6: # less than (first: 0, else: 0)
        if val[0] < val[1]:
            outstream.append(
                    BitStream(hex=hex(1))
                    )
        else:
            outstream.append(
                    BitStream(hex=hex(0))
                    )
        
    elif opID == 7: # equal (yes: 1, no: 0)
        if val[0] == val[1]:
            outstream.append(
                    BitStream(hex=hex(1))
                    )
        else:
            outstream.append(
                    BitStream(hex=hex(0))
                    )
    print(F"{s*layer}- Result: {outstream.bin}, {outstream.uint}")
    return outstream
        
s = "----"
def readStream(instream, layer=0):
    print(F"{s*layer}- Position: {instream.pos}")
    outstream = BitStream()
    if instream[instream.pos:].uint == 0:
        print(F"{s*layer}- Stream exhausted")
    else:
        ver, typ = vers_type(instream)
        print(F"{s*layer}- Version: {ver}, Type: {typ}")
        if typ == 4:
            outstream.append(read_literal(instream))
            print(F"{s*layer}- Found literal: {outstream.uint}")
        else:
            OPstream = []
            if instream.read(1):
                sub_num = instream.read(11).uint
                print(F"{s*layer}- Reading {sub_num} sub-package(s)")
                for i in range(sub_num):
                    print(F"{s*layer}- Package {i+1}:")
                    OPstream.append(readStream(instream, layer+1))
            else:
                sub_len = instream.read(15).uint
                print(F"{s*layer}- Reading sub-packet(s) of length {sub_len}")
                start = instream.pos
                while instream.pos < start + sub_len:
                    print(F"{s*layer}- Package at pos {instream.pos}:")
                    OPstream.append(readStream(instream, layer+1))
            outstream.append(operate(OPstream, typ, layer+1))
                
    return outstream

with open("input", "r") as f:
    in_hex = f.readlines()[0]

in_int = int(in_hex, 16)
in_bin = bin(in_int)
stream = BitStream(hex=in_hex)
        
ver_total = 0
print(F"Stream length: {stream.len}")

out = readStream(stream)
print()
print("- Output -")
print(F"As bin: {out.bin}")
print(F"As int: {out.uint}")
print(F"Total of version number: {ver_total}")
print()
print(F"Position: {stream.pos}/{stream.len}")


print()
print("--- %s seconds ---" % (time.time() - start_time))
