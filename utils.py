import numpy as np

def read_line_by_line(file_path):
    data = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            data.append(line)
    return data

def read_grid(file_path):
    data = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            line = list(line)
            data.append(line)
            print(line)
    data = np.asarray(data, dtype="str")
    return data

def read_grid_and_rest(file_path):
    data = []
    with open(file_path) as f:
        grid, rest = f.read().split("\n\n")
        for line in grid.split("\n"):
            line = line.strip()
            line = list(line)
            data.append(line)
    data = np.asarray(data, dtype="str")
    return data, rest

