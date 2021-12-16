import time
start_time = time.time()

from bitstring import BitStream

with open("input", "r") as f:
    in_hex = f.readlines()[0]

# Examples
#in_hex = "D2FE28"
#in_hex = "8A004A801A8002F478"
#in_hex = "620080001611562C8802118E34"
#in_hex = "C0015000016115A2E0802F182340"
#in_hex = "A0016C880162017C3686B18A3D4780"

# header
#   3 bit version
#   3 bit type
#      -ID==4: literal value
#       x*5 bits. leading 1 in all but last pack
#      -ID!=4: operator
#       next bit 0: 15 bits -> number -> bit-length of sub packets
#       next bit 1: 11 bits -> number of sub packets

in_int = int(in_hex, 16)
in_bin = bin(in_int)
stream = BitStream(hex=in_hex)

def vers_type(instream):
    a_version = instream.read(3).uint
    a_type = instream.read(3).uint
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

def read_stream(instream):
    print(F"--- Position: {instream.pos}, ", end="")
    try:
        ver, typ = vers_type(instream)
        print(F"Version: {ver}, Type: {typ}")
        global ver_total
        ver_total += ver
        
        outstream = BitStream()
        if typ == 4:
            outstream.append(read_literal(instream))
            print(F"Found literal: {outstream.uint}")
        else:
            if instream.read(1): # length type id: 1
                sub_num = instream.read(11).uint
                print(F"Number of sub-packets: {sub_num}")
                for i in range(sub_num):
                    outstream.append(read_stream(instream))
            else:                # length type id: 0
                sub_len = instream.read(15).uint
                print(F"Length of sub-packets: {sub_len}")
                outstream.append(read_stream(instream.read(sub_len)))
        outstream.append(read_stream(instream))
    except:        
        print("Reached end of BitString ---")
        return
        
ver_total = 0
print(F"Stream length: {stream.len}")
read_stream(stream)
        
    

print()
print("--- %s seconds ---" % (time.time() - start_time))
