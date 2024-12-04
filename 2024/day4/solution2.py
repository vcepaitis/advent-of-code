import numpy as np


def check(strs):
    assert len(strs) == 3
    str = ''.join(strs)
    if str == "MAS" or str == "SAM":
        return True
    return False

data = np.genfromtxt("input",dtype=str,delimiter=1)
nx, ny = data.shape

counter = 0

for i in range(1, nx-1):
    for j in range(1, ny-1):
        # diagonals
        diag1 = [data[i+k, j+k] for k in [-1, 0, 1]]
        diag2 = [data[i+k, j-k] for k in [-1, 0, 1]]
        if check(diag1) and check(diag2):
            counter += 1
       
print(f"The counter of part 2 is {counter}")

