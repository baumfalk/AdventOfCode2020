import time
from collections import defaultdict, Counter
from copy import deepcopy
import numpy as np
from itertools import permutations, combinations


content = list(map(lambda s: int(s.strip('\r\n')), open("input.txt").readlines()))


def part1(input, preamble_len=25):
    sums = defaultdict(set)        
    
    for index1, x in enumerate(input[:preamble_len]):
        for index2, y in enumerate(input[:preamble_len]):
            if index1 == index2:
                continue
            lowest_index = min(index1, index2)
            sums[x+y].add(lowest_index)

    for index1, x in enumerate(input):
        if index1 < preamble_len:
            continue
        not_in_sums = x not in sums
        if not_in_sums:
            return x
        too_long_ago_in_sums = max(sums[x]) < (index1 - preamble_len)
        if too_long_ago_in_sums:
            return x
        input_subset = input[(index1-preamble_len+1):(index1+1)]
        for index2, y in enumerate(input_subset):
            real_index2 = index1-preamble_len+1 + index2
            if index1 == real_index2:
                continue
            lowest_index = min(index1, real_index2)
            total = x + y
            sums[total].add(lowest_index)
        pass


def part2(input):
    num_to_find = part1(input)
    for start_index in range(len(input)):
        for end_index in range(start_index,len(input)):
            input_subset = input[start_index:end_index]
            total = sum(input_subset)
            if total == num_to_find:
                return min(input_subset) + max(input_subset)
            if total > num_to_find:
                break
print(part1(content))
print(part2(content))