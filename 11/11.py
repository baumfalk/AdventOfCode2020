import time
from collections import defaultdict, Counter
from copy import deepcopy
import numpy as np
from itertools import permutations


content = list(map(lambda s: s.strip('\r\n'), open("input.txt").readlines()))
"""
Now, you just need to model the people who will be arriving shortly.
 Fortunately, people are entirely predictable and always follow a simple set of rules. 
 All decisions are based on the number of occupied seats adjacent to a given seat 
 (one of the eight positions immediately up, down, left, right, or diagonal from the seat). 
 The following rules are applied to every seat simultaneously:

"""


def count_occupied_seats(grid):
    occupied_cells = [cell for row in grid for cell in row if cell == "#"]
    return len(occupied_cells)

def print_grid(grid, cur_round):
    print("Round", cur_round)
    for row in grid:
        print("".join(row))
    print("-------------")


def part1(input):
    def get_neighbor_indices(row_i, col_i, min_col=0, min_row=0, max_col=1e999, max_row=1e999):
        neighbor_indices = [(row_i + row_delta, col_i + col_delta) for col_delta in (-1, 0, 1) for row_delta in
                            (-1, 0, 1) if not (row_delta == 0 and col_delta == 0)]

        def pos_is_within_grid(row_i, col_i):
            col_within_grid = (min_col <= col_i < max_col)
            row_within_grid = (min_row <= row_i < max_row)
            return col_within_grid and row_within_grid

        neighbor_indices = [(row_i, col_i) for row_i, col_i in neighbor_indices if pos_is_within_grid(row_i, col_i)]
        return neighbor_indices

    def next_state_cell(row_i, col_i, grid):
        cell = grid[row_i][col_i]
        cell_is_empty = cell == "."
        seat_is_occupied = cell == "#"
        if cell_is_empty: return cell

        neighbor_indices = get_neighbor_indices(row_i, col_i, max_col=len(grid[0]), max_row=len(grid), )
        neighbor_cells = [grid[row_i][col_i] for row_i, col_i in neighbor_indices]
        num_occupied_neighbor_seats = len([cell for cell in neighbor_cells if cell == "#"])

        # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        if not seat_is_occupied and num_occupied_neighbor_seats == 0:
            return "#"
        # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
        elif seat_is_occupied and num_occupied_neighbor_seats >= 4:
            return "L"
        # Otherwise, the seat's state does not change.
        else:
            return cell

    def next_state_row(row_i, grid):
        row = grid[row_i]
        next_row = [next_state_cell(row_i, col_i, grid) for col_i in range(len(row))]
        return next_row

    def next_state_grid(grid):
        next_grid = [next_state_row(row_i, grid) for row_i in range(len(grid))]
        return next_grid
    grid = input
    prev_grid = None
    cur_round = 1
    #print_grid(grid, cur_round)
    while prev_grid != grid:
        cur_round += 1
        prev_grid = grid
        grid = next_state_grid(grid)
        #print_grid(grid, cur_round)
    return count_occupied_seats(grid)
    


def part2(input):
    grid = input
    def get_neighbor_deltas(row_i, col_i, min_col=0, min_row=0, max_col=1e999, max_row=1e999):
        neighbor_indices = [(row_delta, col_delta) for col_delta in (-1, 0, 1) for row_delta in
                            (-1, 0, 1) if not (row_delta == 0 and col_delta == 0)]
        return neighbor_indices
    
    def get_nearest_chair_for_vector(row_i, col_i, row_delta, col_delta, grid):
        dist = 1
        while True:
            try:
                neighbor_row_i = row_i + row_delta * dist
                neighbor_col_i = col_i + col_delta * dist
                if neighbor_col_i < 0 or neighbor_row_i < 0:
                    return None
                
                cell = grid[neighbor_row_i][neighbor_col_i]
                if cell != ".":
                    return cell
                dist += 1
            except Exception:
                return None
            
    def get_nearest_chairs(row_i, col_i, grid):
        deltas = get_neighbor_deltas(row_i, col_i, max_row=len(grid), max_col=len(grid[0]))
        return [get_nearest_chair_for_vector(row_i, col_i, row_delta, col_delta, grid) for row_delta, col_delta in deltas]

    def next_state_cell(row_i, col_i, grid):
        cell = grid[row_i][col_i]
        cell_is_empty = cell == "."
        seat_is_occupied = cell == "#"
        if cell_is_empty: return cell

        neighbor_cells = get_nearest_chairs(row_i, col_i, grid)
        
        num_occupied_neighbor_seats = len([cell for cell in neighbor_cells if cell == "#"])

        # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        if not seat_is_occupied and num_occupied_neighbor_seats == 0:
            return "#"
        # it now takes five or more visible occupied seats for an occupied seat to become empty
        elif seat_is_occupied and num_occupied_neighbor_seats >= 5:
            return "L"
        # Otherwise, the seat's state does not change.
        else:
            return cell

    def next_state_row(row_i, grid):
        row = grid[row_i]
        next_row = [next_state_cell(row_i, col_i, grid) for col_i in range(len(row))]
        return next_row

    def next_state_grid(grid):
        next_grid = [next_state_row(row_i, grid) for row_i in range(len(grid))]
        return next_grid

    grid = input
    prev_grid = None
    cur_round = 1
    #print_grid(grid, cur_round)
    while prev_grid != grid:
        #print(cur_round)
        cur_round += 1
        prev_grid = grid
        grid = next_state_grid(grid)
        #print_grid(grid, cur_round)
    return count_occupied_seats(grid)
print(part1(content))
print(part2(content))