import numpy as np


def check(strs):
    assert len(strs) == 4
    str = ''.join(strs)
    if str == "XMAS":
        return True
    return False

data = np.genfromtxt("input",dtype=str,delimiter=1)
nx, ny = data.shape

counter = 0

for i in range(nx):
    for j in range(ny):
        # south
        if i + 3 < nx:
            south = data[i:i+4, j]
            if check(south):
                counter += 1
        # north 
        if i - 3 >= 0:
            north = [data[i-k, j] for k in range(4)]
            if check(north):
                counter += 1
        # east 
        if j + 3 < ny:
            east = data[i, j:j+4]
            if check(east):
                counter += 1
            # southeast
            if i + 3 < nx:
                southeast = [data[i+k, j+k] for k in range(4)]
                if check(southeast):
                    counter += 1
            # northeast
            if i - 3 >= 0:
                northeast = [data[i-k, j+k] for k in range(4)]
                if check(northeast):
                    counter += 1
        # west
        if j - 3 >= 0:
            west = [data[i, j-k] for k in range(4)]
            if check(west):
                counter += 1
            # southwest
            if i + 3 < nx:
                southwest = [data[i+k, j-k] for k in range(4)]
                if check(southwest):
                    counter += 1
            # northwest
            if i - 3 >= 0:
                northwest = [data[i-k, j-k] for k in range(4)]
                if check(northwest):
                    counter += 1

print(f"The counter of part 1 is {counter}")

