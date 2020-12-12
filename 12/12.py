import math
import time
from collections import defaultdict, Counter
from copy import deepcopy
import numpy as np
from itertools import permutations
import re

content = list(map(lambda s: s.strip('\r\n'), open("input.txt").readlines()))
expr = re.compile(r"(.)(\d+)")
content = list(map(lambda s: expr.fullmatch(s).groups(), content))
content = list(map(lambda s: (s[0], int(s[1])), content))
print({x for x in content if x[0] in "LR"})
def part1(input):
    pos_x = 0
    pos_y = 0
    cur_dir = "E"
    
    instr_semantics = {}
    instr_semantics["N"] = (0, 1)
    instr_semantics["E"] = (1, 0)
    instr_semantics["S"] = (0, -1)
    instr_semantics["W"] = (-1, 0)
    
    turn_right_lookup = {}
    turn_right_lookup["N"] = ["E", "S", "W"]
    turn_right_lookup["E"] = ["S", "W", "N"]
    turn_right_lookup["S"] = ["W", "N", "E"]
    turn_right_lookup["W"] = ["N", "E", "S"]

    turn_left_lookup = {}
    turn_left_lookup["N"] = turn_right_lookup["N"][::-1]
    turn_left_lookup["E"] = turn_right_lookup["E"][::-1]
    turn_left_lookup["S"] = turn_right_lookup["S"][::-1]
    turn_left_lookup["W"] = turn_right_lookup["W"][::-1]
    
    
    for instr, amount in input:
        if instr in instr_semantics:
            delta_x, delta_y = instr_semantics[instr]
            pos_x += delta_x*amount
            pos_y += delta_y*amount
        elif instr == "F":
            delta_x, delta_y = instr_semantics[cur_dir]
            pos_x += delta_x*amount
            pos_y += delta_y*amount
        elif instr == "R":
            rot = (amount // 90) - 1
            cur_dir = turn_right_lookup[cur_dir][rot]
        elif instr == "L":
            rot = (amount // 90) - 1
            cur_dir = turn_left_lookup[cur_dir][rot]
    return abs(pos_x)+abs(pos_y), pos_x, pos_y


def part2(input):
    pos_x = 0
    pos_y = 0
    way_point_x = 10
    way_point_y = 1
    cur_dir = "E"

    instr_semantics = {}
    instr_semantics["N"] = (0, 1)
    instr_semantics["E"] = (1, 0)
    instr_semantics["S"] = (0, -1)
    instr_semantics["W"] = (-1, 0)

    turn_right_lookup = {}
    turn_right_lookup["N"] = ["E", "S", "W"]
    turn_right_lookup["E"] = ["S", "W", "N"]
    turn_right_lookup["S"] = ["W", "N", "E"]
    turn_right_lookup["W"] = ["N", "E", "S"]

    turn_left_lookup = {}
    turn_left_lookup["N"] = turn_right_lookup["N"][::-1]
    turn_left_lookup["E"] = turn_right_lookup["E"][::-1]
    turn_left_lookup["S"] = turn_right_lookup["S"][::-1]
    turn_left_lookup["W"] = turn_right_lookup["W"][::-1]

    for instr, amount in input:
        if instr in instr_semantics:
            delta_x, delta_y = instr_semantics[instr]
            way_point_x += delta_x * amount
            way_point_y += delta_y * amount
        elif instr == "F":
            pos_x += way_point_x * amount
            pos_y += way_point_y * amount
        elif instr == "R":
            
            """double x1 = point.x - center.x;
double y1 = point.y - center.y;

double x2 = x1 * Math.cos(angle) - y1 * Math.sin(angle));
double y2 = x1 * Math.sin(angle) + y1 * Math.cos(angle));

point.x = x2 + center.x;
point.y = y2 + center.y;"""
            way_point_x_old = way_point_x
            way_point_y_old = way_point_y
            radians = math.radians(-amount)
            new_waypoint_x = way_point_x_old * math.cos(radians) - way_point_y_old * math.sin(radians)
            new_waypoint_y = way_point_x_old * math.sin(radians) + way_point_y_old * math.cos(radians)

            way_point_x = int(round(new_waypoint_x))
            way_point_y = int(round(new_waypoint_y))
        elif instr == "L":
            way_point_x_old = way_point_x
            way_point_y_old = way_point_y
            radians = math.radians(amount)
            new_waypoint_x = way_point_x_old * math.cos(radians) - way_point_y_old * math.sin(radians)
            new_waypoint_y = way_point_x_old * math.sin(radians) + way_point_y_old * math.cos(radians)

            way_point_x = int(round(new_waypoint_x))
            way_point_y = int(round(new_waypoint_y))
    return abs(pos_x) + abs(pos_y), pos_x, pos_y

print(part1(content))
print(part2(content))