import numpy as np

with open("input") as f:
    n_safe = 0
    n_safe_two = 0
    for l in f:
        levels = np.asarray(l.strip().split(), dtype=int)
        diffs = levels[1:] - levels[:-1]
        ascending = (diffs > 0) & (diffs < 4)
        descending = (diffs > -4) & (diffs < 0)
        n_levels = len(levels)
        if np.all(ascending) or np.all(descending):
            n_safe += 1
            n_safe_two += 1
        else:
            # Part two: remove one element and try again
            for i in range(n_levels):
                removed_levels = np.delete(levels, i)
                diffs = removed_levels[1:] - removed_levels[:-1]
                ascending = (diffs > 0) & (diffs < 4)
                descending = (diffs > -4) & (diffs < 0)
                if np.all(ascending) or np.all(descending):
                    n_safe_two +=1 
                    print(levels, removed_levels)
                    break

print(f"Number of safe reports is {n_safe}")
print(f"Number of safe reports in part two is {n_safe_two}")