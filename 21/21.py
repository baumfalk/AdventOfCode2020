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
    parsed = [(left.split(" "), right[:-1].split(", ")) for left, right in [line.split(" (contains ") for line in input]]
    
    possibilities = dict()
    all_ingredients = Counter()
    for ingredients, allergies in parsed:
        all_ingredients.update(ingredients)
        for allergy in allergies:
            if allergy not in possibilities:
                possibilities[allergy] = set(ingredients)
            possibilities[allergy] = possibilities[allergy].intersection(set(ingredients))
    
    all_possible_allergy_ingredients = set()
    for allergy in possibilities:
        all_possible_allergy_ingredients = all_possible_allergy_ingredients.union((possibilities[allergy]))
        print(allergy, possibilities[allergy])
    print(all_ingredients)
    total=0
    for ingredient in all_ingredients:
        if ingredient not in all_possible_allergy_ingredients:
            total += all_ingredients[ingredient] 

    

    return total


def part2(input):
   

    pass
print(part1(content))
print(part2(content))