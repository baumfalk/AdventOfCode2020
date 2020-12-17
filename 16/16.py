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


#content = list(map(lambda s: s.strip('\r\n'), open("input.txt").readlines()))
content= open("input.txt").read()

def parse_rule(rule):
    rule_head, rule_body = rule.split(":")
    clause_1, clause_2 = rule_body.split(" or ")
    clause_1_start,clause_1_end = clause_1.split("-")
    clause_1_start,clause_1_end = int(clause_1_start), int(clause_1_end)
    clause_2_start, clause_2_end = clause_2.split("-")
    clause_2_start, clause_2_end = int(clause_2_start), int(clause_2_end)
    
    return rule_head, (clause_1_start, clause_1_end), (clause_2_start, clause_2_end)

def parse_ticket_line(line):
    return [int(num) for num in line.split(",")]

def check_val(val, rule):
    rule_head, (clause_1_start, clause_1_end), (clause_2_start, clause_2_end) = rule
    return clause_1_start <= val <= clause_1_end or clause_2_start <= val <= clause_2_end 

def part1(input):
    rules, my_ticket, other_tickets = input.split("\n\n")
    rules = rules.split("\n")
    my_ticket = my_ticket.split("\n")[1]
    other_tickets = other_tickets.split("\n")[1:]
    
    parsed_rules = [parse_rule(rule) for rule in rules]
    my_ticket_parsed = parse_ticket_line((my_ticket))
    other_tickets_parsed = [parse_ticket_line(ticket) for ticket in other_tickets]
    
    ticket_scanning_error_rate = 0
    for ticket in other_tickets_parsed:
        for num in ticket:
            valid_num_for_rules = [check_val(num, rule) for rule in parsed_rules]
            if not any(valid_num_for_rules):
                ticket_scanning_error_rate += num
    return ticket_scanning_error_rate

def part2(input):
    rules, my_ticket, other_tickets = input.split("\n\n")
    rules = rules.split("\n")
    my_ticket = my_ticket.split("\n")[1]
    other_tickets = other_tickets.split("\n")[1:]

    parsed_rules = [parse_rule(rule) for rule in rules]
    my_ticket_parsed = parse_ticket_line((my_ticket))
    other_tickets_parsed = [parse_ticket_line(ticket) for ticket in other_tickets]
    valid_tickets = []
    for ticket in other_tickets_parsed:
        is_valid = True
        for num in ticket:
            valid_num_for_rules = [check_val(num, rule) for rule in parsed_rules]
            if not any(valid_num_for_rules):
                is_valid = False
                break
        if is_valid:
            valid_tickets.append(ticket)
    
    num_valid_tickets = len(valid_tickets)
    for rule in parsed_rules:
        valid_rule_col = defaultdict(int)
        rule_head, (clause_1_start, clause_1_end), (clause_2_start, clause_2_end) = rule
        print(rule_head)
        for ticket in valid_tickets:
            for index, num in enumerate(ticket):
                if check_val(num, rule):
                    valid_rule_col[index] += 1
        for index in valid_rule_col:
            if num_valid_tickets == valid_rule_col[index]:
                print(index, end=" ")
        print()
    """departure location
2     
departure station
14     
departure platform
16    
departure track
1     
departure date
17    
departure time
6    """
    indices = (2,14,16,1,17,6)
    vals = [my_ticket_parsed[index] for index in indices]
    prod = 1
    for val in vals:
        prod *= val
    return prod 

    pass
print(part1(content))
print(part2(content))