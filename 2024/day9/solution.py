import numpy as np
from numba import njit

@njit
def sort_disk(disk):
    ndisk = len(disk)
    for i in range(ndisk):
        if disk[i] == ".":
            for j in range(ndisk-1, i, -1):
                if disk[j] != ".":
                    disk[i] = disk[j]
                    disk[j] = "."
                    break
    return disk
diskmap = str(12345)
# diskmap = str(2333133121414131402)
diskmap = open("input").readline().strip()
disk = []

free = False
id = 0
for input in diskmap:
    if free:
        disk.extend("."*int(input))
    else:
        disk.extend(str(id)*int(input))
        id += 1

    free = not free


disk = sort_disk(disk)
checksum = 0

for i, x in enumerate(disk):
    if x != ".":
        checksum += i*int(x)

print(checksum)