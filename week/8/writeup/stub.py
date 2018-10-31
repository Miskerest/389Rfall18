#!/usr/bin/env python2

import sys
import struct
import itertools


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1
WORD = 4
DWORD = 8
DOUBLE = 8
types = {0x1: "PNG", 0x2 : "DWORDS", 0x3 : "UTF8", 0x4 : "DOUBLES", 0x5 : "WORDS", 0x6 : "COORD", 0x7 : "SEC_REF", 0x9 : "ASCII"}

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
curr = 0
magic, version = struct.unpack("<LL", data[0:8])
curr += 8

time = struct.unpack("<L", data[curr:curr+4])[0]
curr += 4

author = struct.unpack("<ssssssss", data[curr:curr+8])
curr += 8

sections = struct.unpack("<L", data[curr:curr+4])[0]
curr += 4

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIME: %d" % int(time))
print("AUTHOR: %s" % ''.join(author))
print("SECTIONS: %d" % sections)

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
for i in range(0, sections+3):
    print("Section %d:" % i)
    
    stype = struct.unpack("<L", data[curr:curr+4])[0]
    slen = struct.unpack("<L", data[curr+4:curr+8])[0]
    curr += 8
    print("type: %d - %s" % (stype, types[stype]))
    print("length: %d" % slen)

    if slen > 0:
        if (stype == 0x1):
            with open("out_%d.png" % i, "wb") as f:
                f.write("\x89\x50\x4e\x47\x0d\x0a\x1a\x0a")
                f.write(''.join(struct.unpack("<"+slen*"s", data[curr:curr+slen])))

        elif (stype == 0x2):
            svalue = struct.unpack("<"+"LL"*(slen/8), data[curr:curr+slen])
            print(svalue)
        elif stype == 0x5:
            svalue = struct.unpack("<"+"L"*(slen/4), data[curr:curr+slen])
            print("Value: ")
            print(svalue)
        elif stype == 0x6:
            lat,lon = struct.unpack("<ff", data[curr:curr+8])
            print (lat, lon)
        elif stype == 0x7:
            index = struct.unpack("<L", data[curr:curr+4])
            print("Value: %s" % index)
        else:
            svalue = struct.unpack("<"+slen*"s", data[curr:curr+slen])
            print("Value: " + ''.join(svalue))



    curr += slen 
    

    print("\n")