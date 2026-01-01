import sys
sys.path.append("../..")
import numpy as np
from utils import read_grid
from itertools import product

data = read_grid("input")
length = data.shape[0]

def count_neighbours(data: np.array):
    # Make an array to count neighbours
    neighbours_counter = np.zeros_like(data)

    for i in range(length):
        for j in range(length):
            element = data[i, j]
            if element == 1:
                # Increment counter for all neighbouring coordinates
                for move in product((0, -1, 1), (0, -1, 1)):
                    neighbour_i = i + move[0]
                    neighbour_j = j + move[1]
                    # Check boundary conditions
                    if move == (0, 0):
                        continue
                    if neighbour_i < 0 or neighbour_i == length:
                        continue
                    if neighbour_j < 0 or neighbour_j == length:
                        continue
                    neighbours_counter[neighbour_i, neighbour_j] += 1

    return neighbours_counter

# Transform data to something friendlier for numpy
for i in range(length):
    for j in range(length):
        data[i, j] = 1 if data[i, j] == "@" else 0

data = np.asarray(data, dtype=int)
neighbours_counter = count_neighbours(data)

# Part 1 answer
n_rolls = np.sum(neighbours_counter < 4 * data)
print(f"Part 1: {n_rolls}")

# Part 2
# Remove accessible rolls and count again
n_rolls_total = n_rolls
n_rolls_new = None

while n_rolls_new != 0:
    # Keep rolls with more than three neighbours
    neighbours_counter = count_neighbours(data)
    data_new = (neighbours_counter >= 4) * (data)
    neighbours_counter_new = count_neighbours(data_new)
    n_rolls_new = np.sum(neighbours_counter_new < 4 * data_new)
    n_rolls_total += n_rolls_new
    data = data_new

print(f"Part 2: {n_rolls_total}")