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
    nearest_multiple = []
    
    conditions = []
    for offset, bus_time in enumerate(bus_times):
        if bus_time == "x":
            continue
        else:
            conditions.append((int(bus_time), offset))
    
    conditions=sorted(conditions,reverse=True)

    # gejat van https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
    from functools import reduce
    def chinese_remainder(n, a):
        sum = 0
        prod = reduce(lambda a, b: a * b, n)
        for n_i, a_i in zip(n, a):
            p = prod // n_i
            sum += a_i * mul_inv(p, n_i) * p
        return sum % prod

    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1
    

    n,a = (list(zip(*conditions)))
    a = [-num for num in a]
    print(conditions, n, a)
    return(chinese_remainder(n,a))
    # first_num = conditions[0][0]
    # first_offset = conditions[0][1]
    # condition_lambdas = [lambda t: (t+offset) % n == 0 for (n, offset) in conditions]
    # min_i = 100067280294768//first_num
    # #min_i = 0
    # max_i = 1000000000000000//first_num
    # 
    # for i in range(min_i, max_i):
    #     time = i * first_num-first_offset
    #     good_count = 0
    #     for bus_time, offset in conditions[1:]:
    #         if ((time + offset) % bus_time == 0):
    #             if not good_count:
    #                 print(time,end=": ")
    #             print(f"{bus_time}=T", end=" ")
    #             good_count += 1
    #     if good_count > 0:
    #         print(good_count)
    #     if good_count == len(conditions[1:]):
    #         print(time,"is the answer")
    #         break
            
                        
    return conditions
print(part1(content))
print(part2(content))