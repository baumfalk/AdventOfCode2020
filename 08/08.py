import copy
import time
from collections import defaultdict, Counter
from copy import deepcopy
import numpy as np
from itertools import permutations


content = list(map(lambda s: s.strip('\r\n'), open("input.txt").readlines()))
content = list(map(lambda s: s.split(" "), content))



def run_program(input, debug=False):
    acc = 0
    times_visited = defaultdict(int)
    cur_instr_pointer = 0
    running = True
    while running:
        cur_instr, param = input[cur_instr_pointer]
        
        if debug: print(cur_instr, param, acc)
        
        #sign, number = param[0], int(param[1:])
        number = int(param)
        times_visited[cur_instr_pointer] += 1
        already_visited_this_instruction = times_visited[cur_instr_pointer] == 2
        
        if already_visited_this_instruction:
            break
        if cur_instr == "nop":
            cur_instr_pointer += 1
        elif cur_instr == "acc":
            acc += number #(-number) if sign == "-" else number
            cur_instr_pointer += 1
        elif cur_instr == "jmp":
            cur_instr_pointer += number #(-number) if sign == "-" else number
            
        end_of_file = cur_instr_pointer == len(input)
        if end_of_file:
            running = False
    return acc, running

def part1(input):
    return run_program(input)

def part2(input):
    relevant_input_with_index = [(index,(instr, param)) for index,(instr, param) in enumerate(input) if instr in ["jmp", "nop"]]
    for index, (instr, param) in relevant_input_with_index:
        input_altered = copy.deepcopy(input)
        input_altered[index][0] = "nop" if instr == "jmp" else "jmp"
        output, still_running = run_program(input_altered)
        if not still_running:
            return output
        
print(part1(content))
print(part2(content))