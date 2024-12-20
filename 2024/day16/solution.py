import sys
sys.path.append("../..")
from utils import read_grid
from collections import defaultdict
from copy import copy
import numpy as np
np.set_printoptions(threshold=sys.maxsize, linewidth=3000)

def get_node_distance(node1, node2):
    deltay = abs(node1[0] - node2[0])
    deltax = abs(node1[1] - node2[1])
    # no diagonal cases
    return deltax + deltay

if len(sys.argv) == 2:
    f = sys.argv[1]
else:
    f = "input"

grid = read_grid(f)
print(grid)

start = np.where(np.asarray(grid) == "S")
start = (int(start[0][0]), int(start[1][0]))
direction = (0, 1)
print(f"Initial state: {start}")

end = np.where(np.asarray(grid) == "E")
end = (int(end[0][0]), int(end[1][0]))

# find all the nodes
# From wikipedia:
# 1: Create a set of all unvisited nodes: the unvisited set.
unvisited_nodes = {start, end}
distances = {start: 0, end: 1e15}
previous = defaultdict(list)
directions = defaultdict(list)
# east
directions[start] = [(0, 1)]
# 2: Assign to every node a distance from start value: for the starting node, it is zero, and for all other nodes, it is infinity, since initially no path is known to these nodes. During execution, the distance of a node N is the length of the shortest path discovered so far between the starting node and N.
for ix, iy in np.ndindex(grid.shape):
    if grid[ix, iy] == ".":
        unvisited_nodes.add((ix, iy))
        distances[(ix, iy)] = 1e15


# 3: From the unvisited set, select the current node to be the one with the smallest (finite) distance; initially, this is the starting node (distance zero). If the unvisited set is empty, or contains only nodes with infinite distance (which are unreachable), then the algorithm terminates by skipping to step 6. If the only concern is the path to a target node, the algorithm terminates once the current node is the target node. Otherwise, the algorithm continues.
while unvisited_nodes:
    for node in unvisited_nodes:
        break
    distance = distances[node]
    for temp_node in unvisited_nodes:
        temp_distance = distances[temp_node] # to do
        if temp_distance < distance:
            node = temp_node
            distance = temp_distance
    # 4: For the current node, consider all of its unvisited neighbors
    for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        neighbour = copy(node)
        neighbour = (neighbour[0] + direction[0], neighbour[1] + direction[1])
        while grid[neighbour] != "#": 
            if neighbour in unvisited_nodes:
                delta_node = get_node_distance(node, neighbour)
                for current_direction in directions[node]:
                    #  and update their distances through the current node;
                    if current_direction == direction:
                        neighbour_distance = distance + delta_node
                    elif current_direction[0] == -direction[0] and current_direction[1] == -direction[1]:
                        neighbour_distance = distance + 2000 + delta_node
                    else:
                        neighbour_distance = distance + 1000 + delta_node
                    # compare the newly calculated distance to the one currently assigned to the neighbor and assign the smaller one to it. For example, if the current node A is marked with a distance of 6, and the edge connecting it with its neighbor B has length 2, then the distance to B through A is 6 + 2 = 8. If B was previously marked with a distance greater than 8, then update it to 8 (the path to B through A is shorter). Otherwise, keep its current distance (the path to B through A is not the shortest).
                    if neighbour_distance < distances[neighbour]:
                        distances[neighbour] = neighbour_distance
                        previous[neighbour] = [node]
                        directions[neighbour] = [direction]
                    elif neighbour_distance == distances[neighbour]:
                        if node not in previous[neighbour]:
                            previous[neighbour].append(node)
                            directions[neighbour].append(direction)
        # 5: After considering all of the current node's unvisited neighbors, the current node is removed from the unvisited set
        # . Thus a visited node is never rechecked, which is correct because the distance recorded 
        # on the current node is minimal (as ensured in step 3), and thus final. Repeat from to step 3.
            neighbour = (neighbour[0] + direction[0], neighbour[1] + direction[1])

    unvisited_nodes.remove(node)
            
# 6: Once the loop exits (steps 3–5), every visited node contains its shortest distance from the starting node.
grid_print = copy(grid)

def walk_back(paths, seen):
    for path in paths:
        if grid[path] != "S":
            grid_print[path] = "O"
            if path not in seen:
                seen.append(path)
            walk_back(previous[path], seen)
            previous.pop(path)

    return seen

seen = walk_back(previous[end], [start, end])
print(grid_print)
with open("output", "w") as f:
    print(grid_print, file=f)
print(f"Part1: {distances[end]}, part 2: {len(seen)}")
