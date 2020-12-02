content = list(map(lambda s: s.strip('\r\n'), open("input.txt").readlines()))
content_parsed = list(map(lambda s: s.split(" "), content))
content_parsed = list(map(lambda t: ((int(t[0].split("-")[0]),int(t[0].split("-")[1])), t[1][:1], t[2]), content_parsed))

def part1(content_parsed):
    count = 0
    for row in content_parsed:
        (min_num_of_char_occurrences, max_num_of_char_occurrences), char, string = row
        num_of_char_occurrences = string.count(char)

        is_legal_password = min_num_of_char_occurrences <= num_of_char_occurrences <= max_num_of_char_occurrences
        if is_legal_password:
            count += 1
    return count


def part2(content_parsed):
    count = 0
    for row in content_parsed:
        (first_index, second_index), char, string = row

        char_is_on_first_index = string[first_index - 1] == char
        char_is_on_second_index = string[second_index - 1] == char
        char_is_only_on_one_index = char_is_on_first_index ^ char_is_on_second_index

        count += char_is_only_on_one_index

    return count

    pass
print(part1(content_parsed))
print(part2(content_parsed))