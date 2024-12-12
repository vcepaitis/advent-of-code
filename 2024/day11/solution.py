with open("input") as f:
    stones = f.readline().strip().split()

print(stones)
stones = [int(stone) for stone in stones]

for i in range(25):
    print(f"Iteration {i}")
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone = str(stone)
            nsplit = len(stone) // 2
            new_stone_1 = int(str(stone[0:nsplit]))
            new_stone_2 = int(str(stone[nsplit:]))
            new_stones.extend([new_stone_1, new_stone_2])
        else:
            new_stones.append(stone*2024)
    stones = new_stones

print(len(new_stones))