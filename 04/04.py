import time
from collections import defaultdict, Counter
from copy import deepcopy
import numpy as np
from itertools import permutations

import json
content = open("input.txt").read()
content = content.split("\n\n")
content = map(lambda s: s.replace("\n", " "), content)
content = list(map(lambda s: s.split(" "), content))

def part1(input):
    passport_list = []
    for passport in content:
        d = {}
        for b in passport:
            i = b.split(':')
            d[i[0]] = i[1]
        passport_list.append(d)

    passport_elements = set(["byr", "iyr","eyr","hgt", "hcl","ecl","pid","cid"])
    obl_passport_elements =  set(["byr", "iyr","eyr","hgt", "hcl","ecl","pid"])
    num_valid_passports = 0
    for passport in passport_list:
        keys = set(passport.keys())
        all_constraints_satisfied = len(obl_passport_elements.difference(keys)) == 0
        num_valid_passports += all_constraints_satisfied
    return num_valid_passports


def part2(input):
  
   passport_list = []
   for passport in content:
       d = {}
       for b in passport:
           i = b.split(':')
           d[i[0]] = i[1]
       passport_list.append(d)

   passport_elements = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
   obl_passport_elements = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
   num_valid_passports = 0
   
   for passport in passport_list:
        keys = set(passport.keys())
        all_constraints_satisfied = len(obl_passport_elements.difference(keys)) == 0
        valid = True
        bla = """
        byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not."""
        byr_valid = lambda byr: len(byr) == 4 and 1920 <= int(byr) <= 2002
        iyr_valid = lambda iyr: len(iyr) == 4 and 2010 <= int(iyr) <= 2020
        eyr_valid = lambda eyr: len(eyr) == 4 and 2020 <= int(eyr) <= 2030
        def hgt_valid(hgt):
            if not hgt.endswith("in") and not hgt.endswith("cm"):
                return False
            if hgt.endswith("in"):
                num = int(hgt.split("in")[0])
                return 59 <= num <= 76
            if hgt.endswith("cm"):
                num = int(hgt.split("cm")[0])
                return 150 <= num <= 193
            return False
        def hcl_valid(hcl):
            if hcl[0] != "#": return False
            if len(hcl[1:]) != 6: return False
            if not hcl[1:].isalnum(): return False
            return True
        def ecl_valid(ecl):
            valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            return ecl in valid_eye_colors
        pid_valid = lambda pid: len(pid) == 9 and pid.isnumeric()
            
        validation_funcs = [byr_valid, iyr_valid,eyr_valid,hgt_valid,hcl_valid,ecl_valid,pid_valid]
        if all_constraints_satisfied:
            valid = True
            for i, k in enumerate(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
                print(f"{k}: {passport[k]}={validation_funcs[i](passport[k])}")
                valid = valid and validation_funcs[i](passport[k])
            print("Final verdict:",  "VALID" if valid else "INVALID")
            print()

            num_valid_passports += valid
   return num_valid_passports
print(part1(content))
print(part2(content))