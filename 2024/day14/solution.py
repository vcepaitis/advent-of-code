import time
import os
import numpy as np

from PIL import Image, ImageDraw, ImageFont

class Grid():
    def __init__(self, n, m):
        self.n = n
        self.m = m 
        self.robots= []
    def add_robot(self, robot):
        self.robots.append(robot)
    def __str__(self):
        out = ""

        for i in range(self.m):
            for j in range(self.n):

                tile = " "
                for robot in self.robots:
                    if robot.px == j and robot.py == i:
                        # tile += 1
                        tile = "+"
                out += str(tile) 
            out += "\n"
        return out
    def evolve(self):
        for robot in self.robots:
            robot.evolve(self)
    def nrobots_in_quadrants(self):
        quadrant_sums = []
        for i in range(2):
            for j in range(2):
                quadrant_sum = 0
                xmin = (self.n * i // 2) + (i % 2) 
                xmax = (self.n * (i + 1)) // 2
                ymin = (self.m * j // 2) + (j % 2)
                ymax = (self.m * (j + 1)) // 2
                for robot in self.robots:
                    if xmin <= robot.px < xmax and \
                    ymin <= robot.py < ymax:
                        quadrant_sum += 1
                quadrant_sums.append(quadrant_sum)
                # 0 1 2 3 4 X 6 7 8 9 10
                # 0 1 2 X 4 5 6
        return quadrant_sums

    def get_safety_factor(self):
        prod = 1
        quadrant_sums = self.nrobots_in_quadrants()
        for sum in quadrant_sums:
            prod *= sum
        return prod

    def get_max_occupation(self):
        test = set(self.__str__())
        test.remove("\n")
        test = [int(t) for t in test]
        return max(test)
    
    def get_variances(self):
        coords_x = []
        coords_y = []
        for robot in self.robots:
            coords_x.append(robot.px)
            coords_y.append(robot.py)
        return np.var(coords_x), np.var(coords_y)

        
    
    def save_image(self, index):
        lines = self.__str__().split("\n")
        font = ImageFont.load_default()
    
        max_line_length = max(len(line) for line in lines)
        char_width, char_height = font.getbbox("A")[2], font.getbbox("A")[3]
        image_width = max_line_length * 3
        image_height = char_height * len(lines)

        image = Image.new("RGB", (image_width, image_height), "white")
        draw = ImageDraw.Draw(image)

        for i, line in enumerate(lines):
            draw.text((0, i * char_height), line, fill="black", font=font)
        image.save(f"tree_{index}.png")

            

class Robot():
    def __init__(self, px, py, vx, vy):
        self.px = int(px)
        self.py = int(py)
        self.vx = int(vx)
        self.vy = int(vy)
    def evolve(self, grid):
        self.px += self.vx
        self.py += self.vy

        if self.px >= grid.n:
            self.px -= grid.n
        elif self.px < 0:
            self.px += grid.n

        if self.py >= grid.m:
            self.py -= grid.m
        elif self.py < 0:
            self.py += grid.m


grid = Grid(101, 103)
with open("input") as f:
    for l in f:
        p, v = l.strip().split(" ")
        px, py = p.split("=")[1].split(",")
        vx, vy = v.split("=")[1].split(",")
        robot = Robot(px, py, vx, vy)
        grid.add_robot(robot)
variances_x = []
variances_y = []
n = 100000
for i in range(n):
    quadrant_sums = grid.nrobots_in_quadrants()

    if i == 100:
        print("Part 1", grid.get_safety_factor())
    var_x, var_y = grid.get_variances()
    variances_x.append(var_x)
    variances_y.append(var_y)
    if var_x < 400 or var_y < 400:
        grid.save_image(i)
    grid.evolve()

print(np.argmin(variances_x), np.argmin(variances_y))
import matplotlib.pyplot as plt
plt.plot(range(n), variances_x, "+")
plt.plot(range(n), variances_y, "*")
plt.savefig("vars.pdf")
