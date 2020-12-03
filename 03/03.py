import time
from collections import defaultdict, Counter
from copy import deepcopy
import numpy as np
from itertools import permutations


content = list(map(lambda s: s.strip('\r\n'), open("input.txt").readlines()))

def part1(input):
    x_pos = 0
    y_pos = 0
    
    x_delta = 3
    y_delta = 1
    done = False
    
    tree_count = 0
    i = 0
    while not done:
        i+=1
        tree_count += input[y_pos][x_pos] == "#"
        if y_pos == len(input)-1:
            done=True
        x_pos += x_delta
        x_pos = x_pos % len(input[0])
        y_pos += y_delta
        
    return tree_count


def part2(input):
    delta_pairs = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    tree_count_list = []
    
    for x_delta, y_delta in delta_pairs:
        x_pos = 0
        y_pos = 0
        done = False
        
        tree_count = 0
        i = 0
        while not done:
            i += 1
            if (y_pos < len(input)):
                tree_count += input[y_pos][x_pos] == "#"
            if y_pos >= len(input) - 1:
                done = True
            x_pos += x_delta
            x_pos = x_pos % len(input[0])
            y_pos += y_delta
        tree_count_list.append(tree_count)

    return np.prod(tree_count_list), tree_count_list

print(part1(content))
print(part2(content))