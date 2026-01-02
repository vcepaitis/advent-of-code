import sys
sys.path.append("../..")
from utils import read_line_by_line
from collections import defaultdict
import matplotlib.pyplot as plt

data = read_line_by_line("input")
# print(data)

separator_idx = data.index("")
fresh_ranges = []

# Convert ranges
for range_str in data[:separator_idx]:
    lower, upper = range_str.split("-")
    lower = int(lower)
    upper = int(upper)
    fresh_ranges.append([lower, upper])

print(f"The fresh ranges list is {fresh_ranges}")

# Loop over products and check how many are fresh
product_ids = data[separator_idx+1:]

n_fresh = 0

for product_id in product_ids:
    product_id = int(product_id)
    found = False
    for lower, upper in fresh_ranges:
        if product_id >= lower and product_id <= upper:
            found = True
            break
    if found:
        n_fresh += 1

print(f"Part 1: {n_fresh}")

# Part 2 

unique_ranges = []

for lower, upper in fresh_ranges:
    print(f"Considering {lower}-{upper}")
    skip = False
    # Check if this range overlaps with existing ranges
    while True:
        modified = False
        for i, (lower_unique, upper_unique) in enumerate(unique_ranges):
            # Check bounds
            if lower_unique <= lower <= upper_unique and lower_unique <= upper <= upper_unique:
                skip = True
                break
            # New range completely contains existing range - merge them
            elif lower <= lower_unique and upper >= upper_unique:
                unique_ranges.pop(i)
                modified = True
                break
            # New range overlaps with top end of existing range
            elif lower_unique <= lower <= upper_unique:
                lower = upper_unique + 1
                print(f"Modified range due to partial overlap from the top")
                modified = True
                break
            # New range overlaps with bottom end of existing range
            elif lower_unique <= upper <= upper_unique:
                upper = lower_unique - 1
                print(f"Modified range due to partial overlap from the bottom")
                modified = True
                break
        
        if skip:
            break
        if not modified:
            break

    if skip:
        print(f"Skipping {lower}-{upper}")
    else:
        print(f"Adding {lower}-{upper}")
        unique_ranges.append([lower, upper])

range_sum = 0

for unique_lower, unique_upper in unique_ranges:
    range_sum += unique_upper - unique_lower + 1

print(f"Part 2: {range_sum}")

# Debugging plots
fig, ax = plt.subplots()
for i, (lower, upper) in enumerate(fresh_ranges):
    ax.hlines(y=i, xmin=lower, xmax=upper)  # uses data coords
ax.set_xlim(min(l for l, _ in fresh_ranges) - 1, max(u for _, u in fresh_ranges) + 1)
plt.savefig("input_ranges.png")
plt.clf()

fig, ax = plt.subplots()
for i, (lower, upper) in enumerate(unique_ranges):
    ax.hlines(y=i, xmin=lower, xmax=upper)  # uses data coords
ax.set_xlim(min(l for l, _ in unique_ranges) - 1, max(u for _, u in fresh_ranges) + 1)
plt.savefig("output_ranges.png")