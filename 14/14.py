import time
from collections import defaultdict, Counter
from copy import deepcopy
import numpy as np
from itertools import permutations

# complex*i to rotate left/ccw, complex*-i to rotate right/cw
x = 0+0j
direction = 1+0j
# if command == 'L':
#     direction *= 1j**(move // 90)
# if command == 'R':
#     direction /= 1j**(move // 90)


content = list(map(lambda s: s.strip('\r\n'), open("input.txt").readlines()))

def set_bit(v, index, x):
  """Set the index:th bit of v to 1 if x is truthy, else to 0, and return the new value."""
  mask = 1 << index   # Compute mask, an integer with just bit 'index' set.
  v &= ~mask          # Clear the bit indicated by the mask (if x is False)
  if x:
    v |= mask         # If x was True, set the bit indicated by the mask.
  return v            # Return the result, we're done.

def part1(input):
    cur_mask = None
    mem = defaultdict(int)
    for line in input:
        left, right = line.split(" = ")
        if left.startswith("mask"):
            cur_mask = {index: int(val) for index, val in enumerate(reversed(right)) if val != "X"}
        else:
            value = int(right)
            address = int(left[4:-1])
            mem[address] = value
            for bit_index, val in cur_mask.items():
                mem[address] = set_bit(mem[address], bit_index, val)
    return sum([val for val in mem.values()])

def generate_addresses(initial_address, bitmasks):
    for bit_index, val in bitmasks:
        if val != "X":
            real_val = int(val)
            if real_val:
                initial_address = set_bit(initial_address, bit_index, int(val))
    addresses = [initial_address]
    for bit_index, val in bitmasks:
        new_adresses = []
        if val == "X":
            for address in addresses:
                address_0 = set_bit(address, bit_index, 0)
                address_1 = set_bit(address, bit_index, 1)
                new_adresses += [address_0, address_1]
            addresses = new_adresses
    return addresses

def part2(input):
    cur_mask = None
    mem = defaultdict(int)
    for line in input:
        left, right = line.split(" = ")
        if left.startswith("mask"):
            cur_mask = {index: val for index, val in enumerate(reversed(right))}
        else:
            value = int(right)
            address = int(left[4:-1])
            addresses = generate_addresses(address, cur_mask.items())
            for cur_address in addresses:
                mem[cur_address] = value
            # mem[address] = value
            # for bit_index, val in cur_mask.items():
            #     mem[address] = set_bit(mem[address], bit_index, val)
   
    return sum([val for val in mem.values()])
print(part1(content))
print(part2(content))