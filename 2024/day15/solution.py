import sys
sys.path.append("../..")
from utils import read_grid_and_rest
from collections import deque
from tqdm import tqdm
from copy import copy
import numpy as np
np.set_printoptions(threshold=sys.maxsize, linewidth=3000)

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
for instruction in tqdm(instructions):
    # @.
    if instruction == "<":
        test = [pos[0], pos[1]-1]
        test2 = [pos[0], pos[1]-2]
    elif instruction == ">":
        test = [pos[0], pos[1]+1]
        test2 = [pos[0], pos[1]+2]
    elif instruction == "^":
        test = [pos[0]-1, pos[1]]
        test2 = [pos[0]-2, pos[1]]
    elif instruction == "v":
        test = [pos[0]+1, pos[1]]
        test2 = [pos[0]+2, pos[1]]
    else:
        raise ValueError()

    # Easy case: just move
    if grid[*test] == ".":
        grid[*pos] = "."
        grid[*test] = "@"
        pos = test
    # Difficult case: move potentially several crates at once 
    elif grid[*test] == "[" or grid[*test] == "]":
        # The direction in which we're moving
        test_dir = [test2[0] - test[0], test2[1] - test[1]]
        boxes = deque([test])

        if grid[*test] == "[":
            box_right = [test[0], test[1]+1]
            boxes.append(box_right)
        elif grid[*test] == "]":
            box_left = [test[0], test[1]-1]
            boxes.append(box_left)
            
        # determine all boxes that are in the way
        box_coords = []
        while boxes:
            element = boxes.popleft()
            if element not in box_coords:
                box_coords.append(element)

            test_new = [element[0] + test_dir[0], element[1] + test_dir[1]]
            if grid[*test_new] == "[" or grid[*test_new] == "]":
                boxes.append(test_new)
                if test_dir == [-1, 0] or test_dir == [1, 0]:
                    if grid[*test_new] == "[":
                        box_right = [test_new[0], test_new[1]+1]
                        boxes.append(box_right)
                    elif grid[*test_new] == "]":
                        box_left = [test_new[0], test_new[1]-1]
                        boxes.append(box_left)

        # Now let's see if we can actually move all the boxes
        new_grid = copy(grid)
        move = True
        for box in reversed(box_coords):
            new_space = [box[0] + test_dir[0], box[1] + test_dir[1]]
            if new_grid[*new_space] == ".":
                new_grid[*new_space], new_grid[*box] = new_grid[*box], new_grid[*new_space]
            else:
                move = False
                break
        if move:
            new_grid[*test] = "@"
            new_grid[*pos] = "."
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


    # print(f"Move {instruction}:")
    # print(grid)
    # print()

total_coords = 0
for ix, iy in np.ndindex(grid.shape):
    if grid[ix, iy] == "[": # Part 1 : O
        total_coords += 100*ix + iy

print(total_coords)