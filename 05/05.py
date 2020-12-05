import time
from collections import defaultdict, Counter
from copy import deepcopy
import numpy as np
from itertools import permutations


content = list(map(lambda s: s.strip('\r\n'), open("input.txt").readlines()))


def part1(input):
    
    def seat_numbers(row):
        min_row, max_row = 0, 127
        min_col, max_col = 0, 7
        
        for char in row:
            if char == "F":
                max_row = (max_row+min_row+1)/2-1
            if char == "B":
                min_row =  (max_row+min_row+1)/2
            if char == "L":
                max_col = (max_col + min_col + 1) / 2 - 1
            if char == "R":
                min_col = (max_col + min_col + 1) / 2
        seat_id = min_row * 8 + min_col
        return seat_id, (min_row, max_row, max_col, min_col)
    
    answers = []
    for row in input:
        ans, info = seat_numbers(row)
        answers.append(ans)
    return max(answers)


def part2(input):
    def seat_numbers(row):
        min_row, max_row = 0, 127
        min_col, max_col = 0, 7

        for char in row:
            if char == "F":
                max_row = (max_row + min_row + 1) / 2 - 1
            if char == "B":
                min_row = (max_row + min_row + 1) / 2
            if char == "L":
                max_col = (max_col + min_col + 1) / 2 - 1
            if char == "R":
                min_col = (max_col + min_col + 1) / 2
        seat_id = min_row * 8 + min_col
        return seat_id, (min_row, max_row, max_col, min_col)

    answers = []
    for row in input:
        ans, info = seat_numbers(row)
        answers.append(ans)

    answers = sorted(answers)
    offset= min(answers)
    for index, ans in enumerate(answers):
        if(index+offset != ans):
            return(index+offset)
print(part1(content))
print(part2(content))