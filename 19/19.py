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

class Rule(object):
    def __init__(self, rule_name, subclauses=None):
        self.rule_name = rule_name
        self.subclauses = subclauses
    
    def parse(self, string, depth=0):
        for subclause in self.subclauses:
            if len(subclause) == 1:
                parse_tree = subclause[0].parse(string, depth+1)
                if parse_tree:
                    return ParseTree(self.rule_name,depth, [parse_tree])
            elif len(subclause) == 2:
                for i in range(0,len(string)):
                    left, right = string[:len(string)-1-i], string[len(string)-1-i:]
                    left_parse_tree = subclause[0].parse(left, depth+1)
                    right_parse_tree = subclause[1].parse(right, depth + 1)
                    if left_parse_tree and right_parse_tree:
                        return ParseTree(self.rule_name, depth, [left_parse_tree, right_parse_tree])

class RuleAtomic(Rule):
    def __init__(self, rule_name):
        super().__init__(rule_name)
    
    def parse(self, string, depth):
        if string == self.rule_name:
            return ParseLeaf(self.rule_name, depth, string)
        return None

class ParsePart(object):
    def __init__(self, rule, depth):
        self.rule = rule
        self.depth = depth

class ParseLeaf(ParsePart):
    def __init__(self, rule, depth, parsed_value):
        super().__init__(rule, depth)
        self.parsed_value = parsed_value
    
    def __repr__(self):
        print("\t"*self.depth,self.rule,"----", self.parsed_value)

class ParseTree(ParsePart):
    def __init__(self, rule, depth, children):
        super().__init__(rule, depth)
        self.children = children
        
    def __repr__(self):
        print("\t"*self.depth,self.rule)
        for child in self.children:
            print(child)
        
    
def part1(input):
    raw_rules, lines = input.split("\n\n")
    raw_rules = raw_rules.split("\n")
    lines = lines.split("\n")
    rules_lookup = dict()
    parse_raw_rules(raw_rules, rules_lookup)
    
    
    total = 0
    for index, line in enumerate(lines):
        print(index,'/',len(lines))
        parse_tree = rules_lookup["0"].parse(line)
        if parse_tree:
            total += 1
    
    return total

def parse_raw_rules(raw_rules, rules_lookup):
    for raw_rule in raw_rules:
        rule_name, clauses = raw_rule.split(": ")
        subclauses_str = clauses.split(" | ")
        subclauses = []
        if rule_name not in rules_lookup:
            rule = Rule(rule_name)
            rules_lookup[rule_name] = rule
        rule = rules_lookup[rule_name]
        for subclause_str in subclauses_str:
            subclause = []
            rules_str = subclause_str.split(" ")
            for subrule_name in rules_str:
                if subrule_name.startswith("\""):
                    atomic_name = subrule_name[1]
                    rules_lookup[subrule_name] = RuleAtomic(atomic_name)
                elif subrule_name not in rules_lookup:
                    subrule = Rule(subrule_name)
                    rules_lookup[subrule_name] = subrule
                subrule = rules_lookup[subrule_name]
                subclause.append(subrule)
            subclauses.append(subclause)
        rule.subclauses = subclauses

def part2(input):
   

    pass
print(part1(content))
print(part2(content))