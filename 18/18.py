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

def handle_operator(num1, num2, op):
    if op=="+":
        return num1+num2
    elif op=="*":
        return num1*num2
    print("ERROR!")

def evaluate_sum(line):
    last_operator = None
    total = 0
    subsums = []
    op_list = []
    for index, symbol in enumerate(line):
        if symbol.isnumeric():
            num = int(symbol)
            if last_operator:
                total = handle_operator(total, num, last_operator)
            else:
                total = num
        elif symbol in "+*":
            last_operator = symbol
        elif symbol == "(":
            subsums.append(total)
            op_list.append(last_operator)
            total = 0
            last_operator = None
        elif symbol == ")":
            running_total = subsums.pop()
            last_operator = op_list.pop()
            if last_operator:
                total = handle_operator(total, running_total, last_operator)
            last_operator = None

    return total


def evaluate_sum_2(line):
    last_operator = None
    total = 0
    subsums = []
    op_list = []
    for index, symbol in enumerate(line):
        if symbol.isnumeric():
            num = int(symbol)
            if last_operator:
                total = handle_operator(total, num, last_operator)
            else:
                total = num
        elif symbol == "+":
            last_operator = symbol
        elif symbol == "*":
            last_operator = symbol
        elif symbol == "(":
            subsums.append(total)
            op_list.append(last_operator)
            total = 0
            last_operator = None
        elif symbol == ")":
            running_total = subsums.pop()
            last_operator = op_list.pop()
            if last_operator:
                total = handle_operator(total, running_total, last_operator)
            last_operator = None

    return total

def part1(input):
    sums = []
    for index, line in enumerate(input):
        print(index, line)
        sums.append(evaluate_sum(line))
    return sum(sums)


def part2(input):
   

    pass
print(part1(content))
print(part2(content))