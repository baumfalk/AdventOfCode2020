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

def get_neighbors_ids(point):
    x,y,z,w = point #zonder w voor deel 1
    
    #any([dx,dy,dz]): ze zijn niet allemaal 0
    return [(x+dx, y+dy, z+dz, w+dw) for dx in [-1,0,1] for dy in [-1,0,1] for dz in [-1,0,1] for dw in [-1,0,1]if any([dx,dy,dz, dw])]

def get_num_active_neighbors(point, active_cells):
    neighbor_ids = get_neighbors_ids(point)
    num_active_neighbors = sum([neighbor_id in active_cells for neighbor_id in neighbor_ids])
    return num_active_neighbors

def get_next_state_for_cell(point, active_cells):
    num_active_neighbors = get_num_active_neighbors(point, active_cells)
    cell_is_active = point in active_cells
    if cell_is_active:
        return num_active_neighbors in [2, 3]
    else:
        return num_active_neighbors == 3

def get_next_state_for_grid(active_cells):
    all_relevant_cells = set()
    
    for cell in active_cells:
        neighbors = get_neighbors_ids(cell)
        all_relevant_cells.update(neighbors)
        all_relevant_cells.add(cell)
    
    active_cells_next_tick=set()
    
    for cell in all_relevant_cells:
        cell_is_active_next_step = get_next_state_for_cell(cell, active_cells)
        if cell_is_active_next_step:
            active_cells_next_tick.add(cell)
    return active_cells_next_tick

def part1(input):
    z = 0
    w = 0 #zonder w voor deel 1
    active_cells = set()
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            pos = (x,y,z,w)
            is_active = char == "#"
            if is_active:
                active_cells.add(pos)
    
    for i in range(6):
        print(i,len(active_cells))
        active_cells = get_next_state_for_grid(active_cells)
    return len(active_cells)


def part2(input):
   

    pass
print(part1(content))
print(part2(content))