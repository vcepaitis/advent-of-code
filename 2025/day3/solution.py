import sys
sys.path.append("../..")
import numpy as np
from utils import read_line_by_line

data = read_line_by_line("input")
joltage_sum = 0

# def get_max_subsequence(bank):


for bank in data:
    bank = np.asarray([int(b) for b in bank])
    max_indices = np.argmax(bank[:-1], keepdims=True)
    max_value = np.max(bank[:-1])
    joltages = []
    for max_index in max_indices:
        subset = bank[max_index+1:]
        max_subset = np.max(subset)
        joltages.append(max_value*10+max_subset)
    max_joltage = np.max(joltages)
    joltage_sum += max_joltage

print(joltage_sum) # 17383 for part 1
    # print(bank, bank[:-1], max_indices, joltages)

