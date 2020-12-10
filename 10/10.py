import time
from collections import defaultdict, Counter
from copy import deepcopy
from functools import reduce

import numpy as np
from itertools import permutations

content = list(map(lambda s: int(s.strip('\r\n')), open("input.txt").readlines()))


def part1(input):
    srted = sorted(input)
    charging_outlet = [0]
    built_in_adapter = [srted[-1] + 3]
    srted = charging_outlet + srted + built_in_adapter
    diff = zip(srted[:-1],srted[1:])
    diff = list((y-x for (x,y) in diff))
    f = lambda tpl, num: (tpl[0]+1, tpl[1]) if num==1 else (tpl[0], tpl[1]+1)
    
    counts = reduce(f,diff, (0,0))
    
    return counts[0] * counts[1]

def calc_possible_routes(current_index, output_index,num_paths, srted):
    if current_index == output_index:
        return 1
    if current_index in num_paths:
        return num_paths[current_index]
    
    route_length = 0
    for middle_index in range(current_index+1, len(srted)):
        if srted[middle_index]-srted[current_index] <= 3:
            route_length += calc_possible_routes(middle_index, output_index, num_paths, srted)
    num_paths[current_index] = route_length
    return route_length

def part2(input):
    srted = sorted(input)
    charging_outlet = [0]
    built_in_adapter = [srted[-1] + 3]
    srted = charging_outlet + srted + built_in_adapter
    num_paths = dict()
    output = calc_possible_routes(0, len(srted)-1, num_paths, srted)
    
    return output

print(part1(content))
print(part2(content))