import time
from collections import defaultdict, Counter
from copy import deepcopy
import numpy as np
from itertools import permutations


content = list(map(lambda s: s.strip('\r\n'), open("input.txt").readlines()))
content = [line.split(" contain ") for line in content]
content = [(line_content[0], line_content[1].split(",")) for line_content in content]
#content = [(line_content[0], (int(bag_row.split(" ")[0]), " ".join(bag_row.split(" ")[1:])))  for line_content in content for bag_row in line_content[1]]

to_from_dict = {}
from_to_dict = {}
for bag_id, bags in content:
    for bag in bags:
        splitted = bag.strip(" .").split(" ")
        if splitted[0] == "no":
            pass       
        else:
            num = int(splitted[0])
            bag_id_2 = " ".join(splitted[1:-1])
            if bag_id_2 not in to_from_dict:
                to_from_dict[bag_id_2] = dict()
            to_from_dict[bag_id_2][bag_id[:-5]] = num
        
for bag_id, bags in content:
    if bag_id not in from_to_dict:
        from_to_dict[bag_id[:-5]] = dict()
    for bag in bags:
        splitted = bag.strip(" .").split(" ")
        if splitted[0] == "no":
            pass       
        else:
            num = int(splitted[0])
            bag_id_2 = " ".join(splitted[1:-1])
            from_to_dict[bag_id[:-5]][bag_id_2] = num

def part1(input):
    goals = set(["shiny gold"])
    new_goals = set(["shiny gold"])
    prev_set_size = 0
    
    while len(goals) != prev_set_size:
        prev_set_size = len(goals)
        new_new_goals = set()
        for goal in new_goals:
            if goal in input:
                new_new_goals = new_new_goals.union(input[goal].keys())
        new_goals = new_new_goals
        goals = goals.union(new_goals)

    return len(goals)-1


def part2(input):
    def traverse_tree(cur_bag):
        if not len(input[cur_bag]):
            return 0
        else:
            bag_amounts = []
            extra_amounts = []
            for needed_bag in input[cur_bag]:             
                val = input[cur_bag][needed_bag]
                extra_amounts.append(val)
                rec_val = traverse_tree(needed_bag)
                bag_amounts.append(val + val * rec_val)
            return sum(bag_amounts)
        
    amount = traverse_tree(("shiny gold"))
    
    return amount
    

print(part1(to_from_dict))
print(part2(from_to_dict))