content = list(map(lambda s: s.strip('\r\n'), open("input.txt").readlines()))


def part1(input, year=2020):
    int_list = list(map(int,input))
    for index, num in enumerate(int_list):
        other_num = (year - num)
        if other_num in int_list:
            return num * other_num


def part2(input, year=2020):
    int_list = list(map(int, input))

    for index, i in enumerate(int_list):
        for index2, j in enumerate(int_list):
            for index3, k in enumerate(int_list):
                if i + j + k == year:
                    return i * j * k


print(part1(content))
print(part2(content))


def part1_sweet(input, year=2020):
    num_pairs = dict()
    int_list = list(map(int,input))
    for num in int_list:
        if num in num_pairs:
            return num * num_pairs[num]
        other_num = (year - num)
        num_pairs[other_num] = num

def part2_sweet(input, year=2020):
    num_pairs = dict()
    int_list = list(map(int,input))
    for num in int_list:
        for num2 in int_list:
            other_num = year-num-num2
            num_pairs[other_num] = num*num2
    for num in int_list:
        if num in num_pairs:
            return num * num_pairs[num]


print(part1_sweet(content))
print(part2_sweet(content))

def part1_sweet_home_comprehensions(input, year=2020):
    
    int_list = list(map(int,input))
    list_comprh_solution = [num*num2 for num in int_list for num2 in int_list if num+num2 == year]
    return list_comprh_solution[0]

def part2_sweet_home_comprehensions(input, year=2020):
    int_list = list(map(int, input))
    list_comprh_solution = [num * num2 * num3 for num in int_list for num2 in int_list for num3 in int_list if num + num2 + num3 == year]
    return list_comprh_solution[0]

print(part1_sweet_home_comprehensions(content))
print(part2_sweet_home_comprehensions(content))