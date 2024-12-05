from itertools import product, permutations
from copy import copy
pages_dict = {}
inverse_dict = {}
updates = []
sum = 0
sum2 = 0

def check_good(update, rules):
    for (x, y) in rules:
        if update.index(x) > update.index(y):
            return False
    return True

with open("input") as f:
    parsing_pages = True
    for line in f:
        if line == "\n":
            parsing_pages = False
            continue
        if parsing_pages:
            x, y = line.strip().split("|")
            x = int(x)
            y = int(y)
            if x in pages_dict:
                pages_dict[x].append(y)
            else:
                pages_dict[x] = [y]
            if y in inverse_dict:
                inverse_dict[y].append(x)
            else:
                inverse_dict[y] = [x]
        else:
            update = line.strip().split(",")
            update = [int(x) for x in update]
            rules = []
            for x, y in product(update, update):
                if x in pages_dict:
                    if y in pages_dict[x]:
                        rules.append([x, y])
            middle = int(update[len(update)//2])
            good = True
            if check_good(update, rules):
                sum += middle
            else:
                # part 2 - bad updates
                new_update = copy(update)
                tries = 0
                while not check_good(new_update, rules):
                    for (x, y) in rules:
                        index_x = new_update.index(x)
                        index_y = new_update.index(y)
                        if index_x > index_y:
                            new_update[index_y] = x
                            new_update[index_x] = y
                new_middle = int(new_update[len(new_update)//2])
                sum2 += new_middle


print("Part 1 sum is ", sum)
print("Part 2 sum is ", sum2)



        