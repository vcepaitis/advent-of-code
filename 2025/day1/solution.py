import sys
sys.path.append("../..")
from utils import read_line_by_line

import re

data = read_line_by_line("input")

# Split by L/R and number
data = [re.findall(r"[L,R]|\d+", d) for d in data]#[:20]

dial = 50
solution = 0
solution2 = 0

print(f"The dial starts by pointing at {dial}")
for direction, magnitude in data:
    old = dial
    magnitude = int(magnitude)
    if direction == "L":
        dial -= magnitude
    elif direction == "R":
        dial += magnitude

    turns = 0
    # Part 2 
    if dial > 0:
        turns = dial // 100
    elif dial < 0:
        turns = -dial // 100
        if old != 0:
            turns += 1
    elif dial == 0:
        turns = 1
    solution2 += turns

    dial = dial % 100
    if dial == 0:
        solution += 1

    # print(f"The dial is rotated {direction}{magnitude} to point at {dial}; during this rotation it goes through zero {turns}")

print(solution, solution2)