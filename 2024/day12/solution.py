import numpy as np
from copy import copy
from numba import njit


class Region():
    def __init__(self, ix, iy, label):
        self.coords = [(ix, iy)]
        self.label = label
        self.area = 1
        self.perimeter = 4

    def expand(self, data, regions):
        self.data = data
        finished = False
        while not finished:
            coords = copy(self.coords)
            for (ix, iy) in coords:
                for direction in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    new_ix = ix + direction[0]
                    new_iy = iy + direction[1]
                    if (0 <= new_ix < data.shape[0]) and (0 <= new_iy < data.shape[1]):
                        if data[new_ix, new_iy] == self.label:
                            if not plot_in_regions(new_ix, new_iy, regions):
                                self.coords.append((new_ix, new_iy))
                                self.area += 1
                                self.perimeter += 4
                                for direction in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                                    perim_ix = new_ix + direction[0]
                                    perim_iy = new_iy + direction[1]
                                    if (0 <= perim_ix < data.shape[0]) and (0 <= perim_iy < data.shape[1]):
                                        if (perim_ix, perim_iy) in coords:
                                            self.perimeter -= 2

            if len(self.coords) == len(coords):
                finished = True

    def get_label(self):
        return self.label

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter

    def get_coords(self):
        return self.coords

    def get_perimeter_coords(self):
        perimeter_coords = []
        for coord in self.coords:
            n_neighbour = 0
            for direction in ((1,1), (-1, -1), (1, -1), (-1, 1), (0, 1), (0, -1), (1, 0), (-1, 0)):
                if (0 <= coord[0] < data.shape[0]) and (0 <= coord[1] < data.shape[1]):
                    new_x = coord[0] + direction[0]
                    new_y = coord[1] + direction[1]
                    if (new_x, new_y) in self.coords:
                        n_neighbour += 1
            if n_neighbour != 8:

                perimeter_coords.append(coord)

        return perimeter_coords

    def get_sides(self):
        perimeter_coords = self.get_perimeter_coords()
        if len(perimeter_coords) == 1:
            return 4
        corners = 0
        for (x, y) in perimeter_coords:
            coord_left = y - 1
            coord_right = y + 1
            coord_up = x - 1
            coord_down = x + 1

            test_left = False
            test_right = False
            test_up = False
            test_down = False

            if coord_left >= 0:
                if data[x, coord_left] == self.label:
                    test_left = True
            if coord_right < data.shape[1]:
                if data[x, coord_right] == self.label:
                    test_right = True
            if coord_up >= 0:
                if data[coord_up, y] == self.label:
                    test_up = True
            if coord_down < data.shape[0]:
                if data[coord_down, y] == self.label:
                    test_down = True

            test_sum = test_left+test_right+test_up+test_down
            test_corners = 0
            if test_sum == 1:
                test_corners += 2
            elif test_sum == 2:
                if test_left and test_up:
                    test_corners += 1
                    if data[coord_up, coord_left] != self.label:
                        test_corners +=1
                if test_left and test_down:
                    test_corners += 1
                    if data[coord_down, coord_left] != self.label:
                        test_corners +=1
                if test_right and test_up:
                    test_corners += 1
                    if data[coord_up, coord_right] != self.label:
                        test_corners +=1
                if test_right and test_down:
                    test_corners += 1
                    if data[coord_down, coord_right] != self.label:
                        test_corners +=1
            elif test_sum == 3 or test_sum == 4:
                if test_up and test_right and test_down:
                    if data[coord_up, coord_right] != self.label:
                        test_corners += 1
                    if data[coord_down, coord_right] != self.label:
                        test_corners += 1
                if test_up and test_left and test_down:
                    if data[coord_up, coord_left] != self.label:
                        test_corners += 1
                    if data[coord_down, coord_left] != self.label:
                        test_corners += 1
                if test_up and test_left and test_right:
                    if data[coord_up, coord_right] != self.label:
                        test_corners += 1
                    if data[coord_up, coord_left] != self.label:
                        test_corners += 1
                if test_left and test_right and test_down:
                    if data[coord_down, coord_left] != self.label:
                        test_corners += 1
                    if data[coord_down, coord_right] != self.label:
                        test_corners += 1
                if test_sum == 4:
                    test_corners = test_corners // 2
            corners += test_corners
            # print(x, y, test_corners)

        return corners


    def __str__(self):
        out = ""
        for ix in range(self.data.shape[0]):
            for iy in range(self.data.shape[1]):
                if (ix, iy) not in self.coords:
                    out+="."
                else:
                    out+=self.label
            out+="\n"
        return out


def plot_in_regions(ix, iy, regions):
    for region in regions:
        if (ix, iy) in region.get_coords():
            return True
    return False


data = []
regions = []
regions_dict = {}

with open("input") as f:
    for line in f:
        split = list(line.strip())
        data.append(split)

data = np.asarray(data, dtype="str")


for ix, iy in np.ndindex(data.shape):
    # print(ix, iy)
    plot = data[ix, iy]
    if not plot_in_regions(ix, iy, regions):
        region = Region(ix, iy, plot)
        regions.append(region)
        region.expand(data, regions)

total = 0
total_2 = 0
for region in regions:
    area = region.get_area()
    perim = region.get_perimeter()
    sides = region.get_sides()
    label = region.get_label()
    # print(f"A Region of {label} plants with price {area} * {sides} = {area*sides}.")
    # print(region)
    total += area * perim
    total_2 += area * sides
print(f"The total cost is {total}")
print(f"The total bulk cost is {total_2}")