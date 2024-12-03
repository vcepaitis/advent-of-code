left_array = []
right_array = []

with open("input") as f:
    for l in f:
        left, right = l.strip().split()
        left_array.append(int(left))
        right_array.append(int(right))

left_array = sorted(left_array)
right_array = sorted(right_array)

similarity_score = 0
for left in left_array:
    counts = 0
    for right in right_array:
        if right > left:
            break
        if left == right:
            counts += 1
    
    print(left, counts)
    similarity_score += left*counts
print(similarity_score)