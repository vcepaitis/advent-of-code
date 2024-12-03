import re

def parse_match(match):
    first, second = match.lstrip("mul(").rstrip(")").split(",")
    return int(first) * int(second)

with open("input") as f:
    sum = 0
    pattern = r"(mul\([\d]+,[\d]+\))"
    pattern_do = r"mul\([\d]+,[\d]+\)|do\(\)|don't\(\)"
    input_str = "do()"

    for line in f:
        input_str += line.strip()
    matches = re.findall(pattern, input_str)
    matches_do = re.findall(pattern_do, input_str)
    for match in matches:
        sum += parse_match(match)

    print(f"part 1 sum is {sum}")    
    sum2 = 0
    do = True
    for match in matches_do:
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        else:
            if do:
                sum2 += parse_match(match)

    print(f"part 2 sum is {sum2}")    
