import numpy as np
from collections import defaultdict
from itertools import combinations
data = []

with open("input") as f:
    for l in f:
        row = list(l.strip())
        data.append(row)

data = np.asarray(data)
print(data)

# relevant frequencies
values, counts = np.unique_counts(data)

freq_dict = defaultdict(list)


def is_diagonal(first, second):
    dx = abs(first[0] - second[0])
    dy = abs(first[1] - second[1])
    return (dx == 0) or (dy == 0) or (dx == dy)
    

def get_dist(first, second):
    return np.square(first[0] - second[0]) + np.square(first[1] - second[1])

# loop over all positions to find frequencies
for x in range(data.shape[0]):
    for y in range(data.shape[1]):
        freq = data[x, y]
        if freq != ".":
            freq_dict[freq].append((x, y))

freq_dict = {freq: positions for freq, positions in freq_dict.items() if len(positions) > 1}
antinodes = defaultdict(None)
antinodes_2 = defaultdict(None)

for x in range(data.shape[0]):
    for y in range(data.shape[1]):
        pos = (x, y)
        # get distances 
        for freq, test_positions in freq_dict.items():
            # Get all combinations of two antennas
            for pos1, pos2 in combinations(test_positions, 2):
                dx1 = pos1[0] - x
                dy1 = pos1[1] - y
                dx2 = pos2[0] - x
                dy2 = pos2[1] - y
                if ((dx1 * 2 == dx2) and (dy1 * 2 == dy2)) \
                or ((dx2 * 2 == dx1) and (dy2 * 2 == dy1)):
                    antinodes[pos] = True
                if dx1 != 0 and dy1 != 0:
                    if dx2/dx1 == dy2/dy1:
                        antinodes_2[pos] = True 
                if dx2 != 0 and dy2 != 0:
                    if dx1/dx2 == dy1/dy2:
                        antinodes_2[pos] = True


print(len(antinodes))
print(len(antinodes_2))