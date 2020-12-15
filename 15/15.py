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
    starting_nums = [int(num_str) for num_str in input[0].split(",")]
    time_number_was_spoken = defaultdict(int) # contains turns since last occurrence
    time_indexer_penultimate = defaultdict(int) # contains turns since last occurrence

    for index, num in enumerate(starting_nums):
        time_number_was_spoken[num] = (index+1)
    counter = Counter(starting_nums)
    last_number_spoken = starting_nums[-1]
    current_turn=len(starting_nums)+1
    number_of_turns_apart = None
    """
    If that was the first time the number has been spoken, the current player says 0.
Otherwise, the number had been spoken before; 
the current player announces how many turns apart the number is from when it was previously spoken.
    """
    max = 30000000
    while current_turn <= max:
        if current_turn % 10000 == 0:
            print(current_turn, current_turn/max)
        # first time number was spoken, current player says 0
        if counter[last_number_spoken] == 1:
            last_number_spoken = 0
        else:
            last_time_index = time_number_was_spoken[last_number_spoken]
            last_number_spoken = number_of_turns_apart
        number_of_turns_apart = current_turn - time_number_was_spoken[last_number_spoken]
        time_number_was_spoken[last_number_spoken] = current_turn
        counter[last_number_spoken] += 1
        current_turn += 1
    return last_number_spoken


def part2(input):
   

    pass
print(part1(content))
print(part2(content))