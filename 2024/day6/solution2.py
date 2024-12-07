import numpy as np
from copy import deepcopy
from collections import Counter
inputs = []
with open("input") as f:
    for line in f:
        input = line.strip()
        #input = input.replace('#', '1').replace('.', '0').replace('^', '2')
        input = [str(x) for x in input]
        inputs.append(input)

og_data = np.asarray(inputs)
nx ,ny = og_data.shape
nstuck = 0
for x in range(nx):
    for y in range(ny):
        print(x, y, nstuck)
        idx = np.argwhere((og_data != "#") & (og_data!= "."))[0]
        data = deepcopy(og_data)
        if data[x, y] == ".":   
            data[x, y] = "#"
        visited_idx = Counter()
        visited_idx_dir_dict = {}
        inbounds = True
        ntry = 0

        while (inbounds) and (ntry < 1e5):
            ntry +=1 
            dir = data[idx[0], idx[1]]
            # up
            if dir == "^":
                new_idx = idx + [-1, 0]
            elif dir == ">":
                new_idx = idx + [0, 1]
            elif dir == "<":
                new_idx = idx + [0, -1]
            elif dir == "v":
                new_idx = idx + [1, 0]
            if new_idx[0] < 0 or new_idx[0] == nx or new_idx[1] < 0 or new_idx[1] == ny:
                inbounds = False 
                print("finished")
            else:
                test = data[new_idx[0], new_idx[1]]
                if test == "#":
                    if dir == "^":
                        data[idx[0], idx[1]] = ">"
                    elif dir == ">":
                        data[idx[0], idx[1]] = "v"
                    elif dir == "v":
                        data[idx[0], idx[1]] = "<"
                    elif dir == "<":
                        data[idx[0], idx[1]] = "^"
                elif test == ".":
                    string = f"{idx[0]}-{idx[1]}"
                    visited_idx[string] += 1
                    visited_idx_dir_dict[string] = dir

                    data[idx[0], idx[1]] = "."
                    data[new_idx[0], new_idx[1]] = dir
                    idx = new_idx
        if ntry >= 1e5:
            nstuck += 1


print(nstuck)