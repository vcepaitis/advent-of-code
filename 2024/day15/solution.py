import sys
sys.path.append("../..")
from utils import read_grid_and_rest
from copy import copy
import numpy as np
np.set_printoptions(threshold=sys.maxsize, linewidth=300)

if len(sys.argv) == 2:
    f = sys.argv[1]
else:
    f = "input"

grid, rest = read_grid_and_rest(f)
instructions = rest.replace("\n", "")

# Part 2
nx = grid.shape[0]
ny = grid.shape[1]*2
second_grid = np.zeros((nx, ny), str)
for ix, iy in np.ndindex(grid.shape):
    element = grid[ix, iy]
    if element == "#":
        second_grid[ix, 2*iy] = "#"
        second_grid[ix, 2*iy+1] = "#"
    elif element == "O":
        second_grid[ix, 2*iy] = "["
        second_grid[ix, 2*iy+1] = "]"
    elif element == ".":
        second_grid[ix, 2*iy] = "."
        second_grid[ix, 2*iy+1] = "."
    elif element == "@":
        second_grid[ix, 2*iy] = "@"
        second_grid[ix, 2*iy+1] = "."
grid = second_grid

start = np.where(np.asarray(grid) == "@")
pos = (int(start[0][0]), int(start[1][0]))
print("Initial state:")
print(grid)
print()
for instruction in instructions:
    if instruction == "<":
        test = [pos[0], pos[1]-1]
        test2 = [pos[0], pos[1]-2]
        test3 = [pos[0], pos[1]-3]
    elif instruction == ">":
        test = [pos[0], pos[1]+1]
        test2 = [pos[0], pos[1]+2]
        test3 = [pos[0], pos[1]+3]
    elif instruction == "^":
        test = [pos[0]-1, pos[1]]
        test2 = [pos[0]-2, pos[1]]
        test3 = [pos[0]-3, pos[1]]
    elif instruction == "v":
        test = [pos[0]+1, pos[1]]
        test2 = [pos[0]+2, pos[1]]
        test3 = [pos[0]+3, pos[1]]
    else:
        raise ValueError()

    if grid[*test] == ".":
        grid[*pos] = "."
        grid[*test] = "@"
        pos = test
    elif grid[*test] == "[" or grid[*test] == "]":
        test_dir = [test2[0] - test[0], test2[1] - test[1]]
        move = True
        new_grid = copy(grid)
        new_grid[*test] = "@"
        new_grid[*pos] = "."

        if test3[0] < 0 or test3[0] == nx:
            move = False
        if test3[1] < 0 or test3[1] == ny:
            move = False

        while move:

            if new_grid[*test3] == "#":
                move = False
            elif new_grid[*test3] == "[" or new_grid[*test3] == "]":
                test2[0] += test_dir[0]
                test2[1] += test_dir[1]
                test3[0] += test_dir[0]
                test3[1] += test_dir[1]

            elif new_grid[*test3] == ".":

                if new_grid[*test2] == "[":
                    new_grid[*test2] = "]"
                    new_grid[*test3] = "["

                elif new_grid[*test2] == "]":
                    new_grid[*test2] = "["
                    new_grid[*test3] = "]"

                break
        if move:
            grid = new_grid
            pos = test

    # first part 
    # elif grid[*test] == "O":
    #     test_dir = [test2[0] - test[0], test2[1] - test[1]]
    #     move = True
    #     new_grid = copy(grid)
    #     new_grid[*test] = "@"
    #     new_grid[*pos] = "."

    #     while move:
    #         if new_grid[*test2] == "#":
    #             move = False
    #         elif new_grid[*test2] == "O":
    #             test2[0] += test_dir[0]
    #             test2[1] += test_dir[1]
    #         elif new_grid[*test2] == ".":
    #             new_grid[*test2] = "O"
    #             break
    #     if move:
    #         grid = new_grid
    #         pos = test


    print(f"Move {instruction}:")
    print(grid)
    print()

total_coords = 0
for ix, iy in np.ndindex(grid.shape):
    if grid[ix, iy] == "[": # Part 1 : O
        total_coords += 100*ix + iy

print(total_coords)