import numpy as np

data = []

def get_trail(data, ix, iy, ends):
    current = data[ix, iy]
    # print(ix, iy, current, ends)
    if current == 9:
        ends.append(([ix, iy]))
        return ends

    for direction in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        new_ix = ix + direction[0]
        new_iy = iy + direction[1]
        if (0 <= new_ix < data.shape[0]) and (0 <= new_iy < data.shape[1]):
            if data[new_ix, new_iy] == current + 1:
                ends = get_trail(data, new_ix, new_iy, ends) 
    
    return ends


with open("input") as f:
    for l in f:
        l = list(l.strip())
        data.append(l)

data = np.asarray(data, dtype="int")

total = 0
total_distinct = 0
# Iterate over all possible trailheads
for ix, iy in np.ndindex(data.shape):
    trailhead = data[ix, iy]
    if trailhead == 0:
        ends = get_trail(data, ix, iy, [])
        unique = np.unique(ends, axis=0)
        print(f"Trailhead found. Found ends: {ends}, unique: {len(unique)}")
        total += len(unique)
        total_distinct += len(ends)

print(total)
print(total_distinct)