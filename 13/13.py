import time
from collections import defaultdict, Counter
from copy import deepcopy
import numpy as np
from itertools import permutations
import math
# complex*i to rotate left/ccw, complex*-i to rotate right/cw
x = 0+0j
direction = 1+0j
# if command == 'L':
#     direction *= 1j**(move // 90)
# if command == 'R':
#     direction /= 1j**(move // 90)


content = list(map(lambda s: s.strip('\r\n'), open("input.txt").readlines()))
content = [line.split(",") for line in content]

def part1(input):
    start_time = int(input[0][0])
    bus_times = input[1]
    nearest_multiple = []
    
    for index, bus_time in enumerate(bus_times):
        if bus_time == "x":
            continue
        else:
            bus_time = int(bus_time)
            earliest_time = (math.ceil(start_time / bus_time) * bus_time)
            time_diff = earliest_time - start_time
            nearest_multiple.append((earliest_time, bus_time, bus_time * time_diff))

    nearest_multiple = sorted(nearest_multiple)
    
    return nearest_multiple[0]


def part2(input):
    bus_times = input[1]
    
    conditions = []
    for offset, bus_time in enumerate(bus_times):
        if bus_time == "x":
            continue
        else:
            conditions.append((int(bus_time), offset))
    
    conditions=sorted(conditions,reverse=True)

    for bus_time, offset in conditions:
        print(f"(t + {offset}) mod {bus_time} = 0", end=", ")
    print()
                        
    return conditions
print(part1(content))
print(part2(content))