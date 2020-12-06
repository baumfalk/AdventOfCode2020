import time
from collections import defaultdict, Counter
from copy import deepcopy
import numpy as np
from itertools import permutations


#content = list(map(lambda s: s.strip('\r\n'), open("input.txt").readlines()))
content = open("input.txt").read()
content = content.split("\n\n")
content = list(map(lambda s: s.split("\n"), content))

def part1(input):
    total = 0
    for group in input:
        total_group_answers = set()
        for answers in group:
            total_group_answers = total_group_answers.union(answers)
        print(total_group_answers)
        total += len(total_group_answers)
        
    return total


def part2(input):
    total = 0
    for group in input:
        total_group_answers = set("abcdefghijklmnopqrstuvwxyz")
        for answers in group:
            total_group_answers = total_group_answers.intersection(answers)
        print(total_group_answers)
        total += len(total_group_answers)

    return total

    pass
print(part1(content))
print(part2(content))