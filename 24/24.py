import collections
import re
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
#content = open("input.txt").read()

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed


def HexagonCell(object):
    def __init__(self):
        self.east = None
        self.south_east = None
        self.south_west = None
        self.west = None
        self.north_west = None
        self.north_east = None

@timeit
def part1(input):
    grid = defaultdict(bool)
    for line in input:
        x, y = instr_to_coords(line)
        grid[(x,y)] = not grid[(x,y)]
    
    return(sum(grid.values()))


def instr_to_coords(line):
    new_line = line.replace("se", "SE ").replace("sw", "SW ").replace("nw", "NW ").replace("ne", "NE ").replace("w","W ").replace("e", "E ").strip().lower().split()
    lookup=dict()
    lookup["nw"] = (-5, 10)
    lookup["sw"] = (-5, -10)
    lookup["ne"] = (5, 10)
    lookup["se"] = (5, -10)
    lookup["w"] = (-10, 0)
    lookup["e"] = (10, 0)
    x, y = 0, 0
    for instr in new_line:
        dx, dy = lookup[instr]
        x, y = x + dx, y + dy
    return x, y

def adjacent_tiles(x,y):
    lookup = dict()
    lookup["nw"] = (-5, 10)
    lookup["sw"] = (-5, -10)
    lookup["ne"] = (5, 10)
    lookup["se"] = (5, -10)
    lookup["w"] = (-10, 0)
    lookup["e"] = (10, 0)
    
    return [(x+lookup[dir][0], y+lookup[dir][1]) for dir in lookup]

def sum_of_black_neighbors(x,y, grid):
    neighbors = adjacent_tiles(x,y)
    total = sum([grid[(x,y)] for x,y in neighbors if (x,y) in grid])
    return total

WHITE = False
BLACK = True

@timeit
def part2(input):
    """Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
    Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
    Here, tiles immediately adjacent means the six tiles directly touching the tile in question.

    The rules are applied simultaneously to every tile; put another way, it is first determined which tiles need to be 
    flipped, then they are all flipped at the same time."""
    grid = {}
    for line in input:
        x, y = instr_to_coords(line)
        if (x,y) not in grid:
            grid[(x, y)] = BLACK
        else:
            grid[(x, y)] = not grid[(x, y)]
    
    
    for i in range(1,101):
        new_grid = {}
        for x, y in grid:
            calculate_next_state_for_self(grid, new_grid, x, y)
            calculate_next_state_for_neighbors(grid, new_grid, x, y)
        grid = new_grid
        print(f"Day {i}: {sum(grid.values())}")
    pass


def calculate_next_state_for_self(grid, new_grid, x, y):
    num_black_neighbors = sum_of_black_neighbors(x, y, grid)
    next_state_of_cell(grid, new_grid, num_black_neighbors, x, y)


def calculate_next_state_for_neighbors(grid, new_grid, x, y):
    neighbors = adjacent_tiles(x, y)
    for neighbor in neighbors:
        if neighbor not in grid and neighbor not in new_grid:
            (x_neighbor, y_neighbor) = neighbor
            num_black_neighbors_of_neighbor = sum_of_black_neighbors(x_neighbor, y_neighbor, grid)
            next_state_of_cell(grid, new_grid, num_black_neighbors_of_neighbor, x_neighbor, y_neighbor)


def next_state_of_cell(grid, new_grid, num_black_neighbors, x, y):
    is_black = grid[(x, y)] if (x,y) in grid else False
    if is_black and num_black_neighbors == 0 or num_black_neighbors > 2:
        new_grid[(x, y)] = WHITE
    elif not is_black and num_black_neighbors == 2:
        new_grid[(x, y)] = BLACK
    else:
        new_grid[(x, y)] = grid[(x, y)] if (x,y) in grid else WHITE


print(part1(content))
print(part2(content))