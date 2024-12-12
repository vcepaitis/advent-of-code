from collections import Counter

with open("input") as f:
    stones = f.readline().strip().split()

print(stones)
stones = [int(stone) for stone in stones]
stones_dict = Counter()
for stone in stones:
    stones_dict[stone] += 1

print(stones_dict)

for i in range(75):
    print(f"Iteration {i}")
    new_stones_dict = Counter()
    for stone, count in stones_dict.items():
        if stone == 0:
            new_stone = 1
            new_stones_dict[new_stone] += count
        elif len(str(stone)) % 2 == 0:
            stone = str(stone)
            nsplit = len(stone) // 2
            new_stone_1 = int(str(stone[0:nsplit]))
            new_stone_2 = int(str(stone[nsplit:]))
            new_stones_dict[new_stone_1] += count
            new_stones_dict[new_stone_2] += count
        else:
            new_stones_dict[stone*2024] += count
    stones_dict = new_stones_dict

total = 0
for stone, count in stones_dict.items():
    total += count

print(total)