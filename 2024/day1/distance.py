left_array = []
right_array = []

with open("input") as f:
    for l in f:
        left, right = l.strip().split()
        left_array.append(int(left))
        right_array.append(int(right))

left_array = sorted(left_array, reverse=True)
right_array = sorted(right_array, reverse=True)
distances = [abs(left - right) for (left, right) in zip(left_array, right_array)]
print(sum(distances))