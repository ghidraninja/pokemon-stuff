#!/usr/bin/env python3

import sys

MEW_TRAINER_ADDR = 0x2a9b
SWIMMER_ADDR = 0x2a0a
GAMBLER_ADDR = 0x2a79
YOUNGSTER_ADDR = 0x2a9d

f = open(sys.argv[1], "rb+")
data = bytearray(f.read())

if(data[MEW_TRAINER_ADDR] & 0x4):
	print("Route 24 trainer already fought. patching.")
	data[MEW_TRAINER_ADDR] ^= 0x4

if(data[SWIMMER_ADDR] & 0x8):
	print("Swimmer trainer already fought. patching.")
	data[SWIMMER_ADDR] ^= 0x8

if(data[GAMBLER_ADDR] & 0x4):
	print("Gambler trainer already fought. patching.")
	data[GAMBLER_ADDR] ^= 0x4

if(data[YOUNGSTER_ADDR] & 0x4):
	print("Youngster trainer already fought. patching.")
	data[YOUNGSTER_ADDR] ^= 0x4

# LiveOverflow checksum code
checksum = 0xff
for c in data[0x2598:0x3523]:
	checksum -= c
data[0x3523] = checksum&0xff
f.seek(0,0)
f.write(data)

print("You are now ready to catch mew!")
