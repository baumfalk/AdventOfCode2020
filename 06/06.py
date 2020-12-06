import time
from collections import defaultdict, Counter
from copy import deepcopy
from functools import reduce

import numpy as np
from itertools import permutations


#content = list(map(lambda s: s.strip('\r\n'), open("input.txt").readlines()))
content = open("input.txt").read()
content = content.split("\n\n")
content = list(map(lambda s: s.split("\n"), content))

def part1(input):
    union = lambda a, b: set(a).union(b)
    r = lambda g: len(reduce(union, g))
    total = sum(map(r, input))
       
    return total


def part2(input):
    intersect = lambda a, b: set(a).intersection(b)
    r = lambda g: len(reduce(intersect, g))
    total = sum(map(r, input))

    return total

print(part1(content))
print(part2(content))