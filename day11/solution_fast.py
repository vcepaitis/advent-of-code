import sys
sys.setrecursionlimit(100000)

rules = {0: [1]}

def split_stone(stone, stones, n=0, nmax=5):
    # Can no longer split
    if n == nmax:
        return stones + [stone]

    if stone in rules:
        for new_stone in rules[stone]:
            stones = split_stone(new_stone, stones, n+1, nmax)

    elif stone == 0:
        stones = split_stone(1, stones, n+1, nmax)

    elif len(str(stone)) % 2 == 0:
        stone = str(stone)
        nsplit = len(stone) // 2
        new_stone_1 = int(str(stone[0:nsplit]))
        new_stone_2 = int(str(stone[nsplit:]))
        rules[int(stone)] = [new_stone_1, new_stone_2]
        stones = split_stone(new_stone_1, stones, n+1, nmax)
        stones = split_stone(new_stone_2, stones, n+1, nmax)
    else:
        rules[stone] = [stone*2024]
        stones = split_stone(stone*2024, stones, n+1, nmax)

    return stones


with open("input") as f:
    stones = f.readline().strip().split()

stones = [int(stone) for stone in stones]

new_stones = []

for stone in stones:
    split_stones = split_stone(stone, [], n=0, nmax=25)
    new_stones.extend(split_stones)

print(len(new_stones))
