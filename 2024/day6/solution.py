import numpy as np

inputs = []
with open("input") as f:
    for line in f:
        input = line.strip()
        #input = input.replace('#', '1').replace('.', '0').replace('^', '2')
        input = [str(x) for x in input]
        inputs.append(input)

data = np.asarray(inputs)
nx ,ny = data.shape
idx = np.argwhere((data != "#") & (data!= "."))[0]
visited_idx = [list(idx)]
inbounds = True
while inbounds:
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
        print("out of bounds")
        inbounds = False 
        if list(idx) not in visited_idx:
            visited_idx.append(list(idx))
        break
    test = data[new_idx[0], new_idx[1]]
    print(idx, dir, test)
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
        if list(idx) not in visited_idx:
            visited_idx.append(list(idx))
        data[idx[0], idx[1]] = "."
        data[new_idx[0], new_idx[1]] = dir
        idx = new_idx

print(len(visited_idx))

