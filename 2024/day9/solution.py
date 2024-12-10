import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
from numba import njit
from collections import defaultdict

# @njit
def sort_disk(disk):
    ndisk = len(disk)
    j_current = ndisk-1
    for i in range(ndisk):
        if disk[i] == ".":
            for j in range(j_current, i, -1):
                if disk[j] != ".":
                    disk[i] = disk[j]
                    disk[j] = "."
                    j_current = j
                    break

            
    return disk

@njit
def defragment_disk(disk):
    ndisk = len(disk)
    i = 0
    j = ndisk - 1
    moved = []

    while j >= i:
        test = disk[i]
        # find the first empty space
        if test != ".":
            i += 1
            continue
        else:
            i_start = i
        file = disk[j]
        # move file at most once
        if file in moved:
            # print("Already moved")
            j -= 1
            continue
        # go until non-empty space found
        elif file == ".":
            j -= 1
        else:
            # number of required free spaces
            nreq = 1
            while disk[j-nreq] == file:
                nreq += 1
            # print(f"found file id {file} of length {nreq}. Checking if there's space starting from {i}")
            # find if any free space can be used
            nfree = 0
            ifree = i
            for k in range(i, j):
                if nreq <= nfree:
                    # swapping
                    for n in range(nreq):
                        disk[ifree+n] = file
                        disk[j-n] = "."
                    i = i_start
                    moved.append(file)
                    break
                # increment free disk space counter
                if disk[k] == ".":
                    if ifree == -1:
                        ifree = k
                    nfree += 1
                # reset free disk space counter
                else:
                    nfree = 0
                    ifree = -1
            # check next file
            j -= nreq

    return disk


diskmap = str(12345)
diskmap = str(2333133121414131402)
diskmap = open("input").readline().strip()
disk = []

free = False
id = 0
for input in diskmap:
    if free:
        disk.extend("."*int(input))
    else:
        disk.extend([str(id)]*int(input))
        id += 1

    free = not free

disk = np.asarray(disk)
disk = defragment_disk(disk)
checksum = 0

for i, x in enumerate(disk):
    if x != ".":
        checksum += i*int(x)

print(checksum)