import sys
sys.path.append("../..")
import numpy as np
from utils import read_line_by_line

data = read_line_by_line("input")
joltage_sum = 0


def get_max_joltage_configuration(bank: list, length: int, batteries: list):
    if length == 1:
        max_index = np.argmax(bank)
        batteries.append(bank[max_index])
        return batteries
    else:
        allowed_batteries = bank[:-length+1]
        max_index = np.argmax(allowed_batteries, keepdims=True)[0]
        batteries.append(bank[max_index])
        sub_bank = bank[max_index+1:]
        return get_max_joltage_configuration(sub_bank, length-1, batteries)
    

def get_configuration_joltage(configuration: list):
    joltage = 0
    for i in range(len(configuration)):
        joltage += configuration[i] * (10 ** ( len(configuration) - i - 1))
    return joltage

joltage_sum_1 = 0
joltage_sum_2 = 0

for bank in data:
    bank = np.asarray([int(b) for b in bank])
    batteries_1 = get_max_joltage_configuration(bank, 2, []) 
    batteries_2 = get_max_joltage_configuration(bank, 12, [])
    joltage_1 = get_configuration_joltage(batteries_1)
    joltage_2 = get_configuration_joltage(batteries_2)
    joltage_sum_1 += joltage_1
    joltage_sum_2 += joltage_2

print(joltage_sum_1, joltage_sum_2)

