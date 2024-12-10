import numpy as np
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
        if test != ".":
            i += 1
            continue
        file = disk[j]

        if file in moved:
            # print("Already moved")
            j -= 1
            continue
        elif file == ".":
            j -= 1
        else:
            nreq = 1
            while disk[j-nreq] == file:
                nreq += 1
            print(f"found {file} of length {nreq}. Checking if there's space starting from {i}")
            nfreemax = 0
            ifreemax = i
            nfree = 0
            ifree = i
            for k in range(i, j-nreq):
                if nreq <= nfreemax:
                    # swapping
                    # print("Found enough space")
                    for n in range(nreq):
                        disk[ifreemax+n] = file
                        disk[j-n] = "."
                    # print("new disk", disk)
                    i = 0
                    moved.append(file)
                    break
                if disk[k] == ".":
                    nfree += 1
                else:
                    if nfree > nfreemax:
                        ifreemax = ifree
                        nfreemax = nfree
                    nfree = 0
                    ifree = k+1
            # print(f"Found {nfreemax} space starting at {ifreemax}")
            # print("Going to next file")
            # check next file
            j -= nreq

    return disk
        

diskmap = str(12345)
diskmap = str(233313312141413140231083)
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
print(disk)
disk = defragment_disk(disk)
print(disk)
checksum = 0

for i, x in enumerate(disk):
    if x != ".":
        checksum += i*int(x)

print(checksum)