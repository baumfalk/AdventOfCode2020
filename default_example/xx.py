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


def part1(input):
    pass


def part2(input):
   

    pass
print(part1(content))
print(part2(content))