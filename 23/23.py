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

@timeit
def part1(input):
    cups = list(input[0])
    cups = list(map(int, cups))
    current_cup_index = 0
    all_cups = set(cups)
    for i in range(1,101):
        print(f"-- move {i} --")
        current_cup = cups[current_cup_index]
        print(f"current cup: {current_cup}")
        print(f"cups: {cups}")
        """The crab picks up the three cups that are immediately clockwise of the current cup. 
        They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle."""
        three_cups = cups[(current_cup_index+1):(current_cup_index+4)]
        if len(three_cups) <3:
            remaining_number = 3 - len(three_cups)
            three_cups += cups[:remaining_number]
        print(f"pick up: {three_cups}")
        for cup in three_cups:
            cups.remove(cup)
        """The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. If this 
        would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup 
        that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's 
        label, it wraps around to the highest value on any cup's label instead."""
        destination_cup = current_cup -1
        if destination_cup not in all_cups:
            destination_cup = max(all_cups)
        while destination_cup in three_cups:
            destination_cup -= 1
            if destination_cup not in all_cups:
                destination_cup = max(all_cups)
        destination_cup_index = [i for i, val in enumerate(cups) if val==destination_cup][0]
        """
        The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. 
        They keep the same order as when they were picked up.
        """
        cups_left, cups_right = cups[:destination_cup_index+1], cups[(destination_cup_index+1):]
        cups = cups_left + three_cups + cups_right
        print(f"destination: {cups_left[-1]}")
        assert(destination_cup==cups_left[-1])
        """The crab selects a new current cup: the cup which is immediately clockwise of the current cup."""
        current_cup_index = [i for i, val in enumerate(cups) if val==current_cup][0]
        current_cup_index = (current_cup_index +1) % len(cups)
        
    one_index = [i for i, val in enumerate(cups) if val==1][0]
    final_list = map(str,cups[(one_index+1):] + cups[:one_index])
    return "".join(final_list)

@timeit
def part1_b(input):
    cups = list(input[0])
    cups = list(map(int, cups))
    print(cups)
    max_cup_num = max(cups)
    #extra_cups = list(range(max_cup_num, 1000001))
    #cups = cups + extra_cups

    lookup = dict()
    prev_cup = None
    prev_el = None
    for cup in cups:
        if prev_cup in lookup:
            prev_el = lookup[prev_cup]
        el = LinkedListElement(prev_el, None, cup)
        if prev_el:
            prev_el.right = el
        prev_cup = cup
        prev_el = None
        lookup[cup] = el

    first_el = lookup[cups[0]]
    last_el = lookup[cups[-1]]
    first_el.left = last_el
    last_el.right = first_el

    current_cup = first_el
    n = 100
    for i in range(1, n + 1):
        if i % 100000 == 0:
            print(i, i / n)
        # print(f"-- move {i} --")
        # print(f"current cup: {current_cup}")
        # print(f"cups: {cups}")
        """The crab picks up the three cups that are immediately clockwise of the current cup. 
        They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle."""
        three_cups = [current_cup.right, current_cup.right.right, current_cup.right.right.right]

        current_cup.right = three_cups[-1].right
        #three_cups[-1].left = current_cup

        #three_cups[0].left = None
        three_cups[-1].right = None

        three_cups_vals = set([cup.value for cup in three_cups])
        """The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. If this 
        would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup 
        that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's 
        label, it wraps around to the highest value on any cup's label instead."""
        destination_cup_val = current_cup.value - 1
        if destination_cup_val < 1:
            destination_cup_val = max_cup_num
        while destination_cup_val in three_cups_vals:
            destination_cup_val -= 1
            if destination_cup_val < 1:
                destination_cup_val = max_cup_num
        destination_cup = lookup[destination_cup_val]
        """
        The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. 
        They keep the same order as when they were picked up.
        """
        neighbor_of_dest_cup = destination_cup.right

        destination_cup.right = three_cups[0]
        #three_cups[0].left = destination_cup
        #neighbor_of_dest_cup.left = three_cups[-1]

        three_cups[-1].right = neighbor_of_dest_cup

        """The crab selects a new current cup: the cup which is immediately clockwise of the current cup."""
        current_cup = current_cup.right

    one_el = lookup[1]
    cur_el = one_el.right
    output = []
    while cur_el != one_el:
        output.append(str(cur_el.value))
        cur_el = cur_el.right
    return "".join(output)

class LinkedListElement(object):
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

@timeit
def part2(input):
    cups = list(input[0])
    cups = list(map(int, cups))
    print(cups)
    max_cup_num = max(cups)
    extra_cups_num = 1000000
    extra_cups = list(range(max_cup_num+1, extra_cups_num+1))
    cups = cups + extra_cups
    max_cup_num = max(cups)
    print(max_cup_num)
    lookup = dict()
    prev_cup = None
    prev_el = None
    for cup in cups:
        if prev_cup in lookup:
            prev_el = lookup[prev_cup]
        el = LinkedListElement(prev_el, None, cup)
        if prev_el:
            prev_el.right = el
        prev_cup = cup
        prev_el = None
        lookup[cup] = el
    
    first_el = lookup[cups[0]]
    last_el = lookup[cups[-1]]
    first_el.left = last_el
    last_el.right = first_el
    
    current_cup = first_el
    n = 10000000
    for i in range(1, n+1):
        if i % (n//4) == 0:
            print(i, i/n)
        #print(f"-- move {i} --")
        #print(f"current cup: {current_cup}")
        #print(f"cups: {cups}")
        """The crab picks up the three cups that are immediately clockwise of the current cup. 
        They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle."""
        three_cups = [current_cup.right, current_cup.right.right, current_cup.right.right.right]
        
        current_cup.right = three_cups[-1].right
        three_cups[-1].left = current_cup
        
        three_cups[0].left = None
        three_cups[-1].right = None
        
        three_cups_vals = set([cup.value for cup in three_cups])
        """The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. If this 
        would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup 
        that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's 
        label, it wraps around to the highest value on any cup's label instead."""
        destination_cup_val = current_cup.value - 1
        if destination_cup_val < 1:
            destination_cup_val = max_cup_num
        while destination_cup_val in three_cups_vals:
            destination_cup_val -= 1
            if destination_cup_val < 1:
                destination_cup_val = max_cup_num
        destination_cup = lookup[destination_cup_val]
        """
        The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. 
        They keep the same order as when they were picked up.
        """
        neighbor_of_dest_cup = destination_cup.right
        
        destination_cup.right = three_cups[0]
        #three_cups[0].left = destination_cup
        neighbor_of_dest_cup.left = three_cups[-1]
        
        three_cups[-1].right = neighbor_of_dest_cup
        
        """The crab selects a new current cup: the cup which is immediately clockwise of the current cup."""
        current_cup = current_cup.right

    one_el = lookup[1]
    num_1,num_2 = one_el.right,one_el.right.right
    print(num_1.value, num_2.value)
    return num_1.value*num_2.value
print(part1_b(content))
print(part2(content))