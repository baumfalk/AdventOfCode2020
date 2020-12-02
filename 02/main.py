content = list(map(lambda s: s.strip('\r\n'), open("input.txt").readlines()))
content_parsed = list(map(lambda s: s.split(" "), content))
content_parsed = list(map(lambda t: ((int(t[0].split("-")[0]),int(t[0].split("-")[1])), t[1][:1], t[2]), content_parsed))

def part1(content_parsed):
    count = 0
    for row in content_parsed:
       rang, char, string = row
       low,high = rang
       num_chars = len(list(filter(lambda c: c == char, string)))
       if num_chars >= low and num_chars <= high:
           count +=1
    return count


def part2(content_parsed):
    count = 0
    for row in content_parsed:
        rang, char, string = row
        low, high = rang
        meta_count = 0
        meta_count += string[low-1] == char
        meta_count += string[high-1] == char
        if meta_count == 1:
            count+=1
            
    return count

    pass
print(part1(content_parsed))
print(part2(content_parsed))