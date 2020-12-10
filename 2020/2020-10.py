from utils import timed

from collections import Counter

with open('inputs/2020-10.txt') as f:
    adapters = list(map(int, f.read().splitlines()))

@timed
def part_one(adapters):
    adapters += [0, max(adapters) + 3]
    adapters.sort()
    jolt_differences = [adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)]
    counter = Counter(jolt_differences)
    return counter[1] * counter[3]

@timed
def part_two(adapters):
    adapters += [0, max(adapters) + 3]
    adapters.sort()
    combinations = 1
    i = 0
    while i < len(adapters) - 2:
        if i + 4 < len(adapters) and adapters[i + 4] == adapters[i] + 4:
            combinations *= 7  # 7 combinations of adapters for a 5-chain of adapters each 1 jolt apart
            i += 4
        elif i + 3 < len(adapters) and adapters[i + 3] == adapters[i] + 3:
            combinations *= 4
            i += 3
        elif adapters[i + 2] in (adapters[i] + 3, adapters[i] + 2):
            combinations *= 2
            i += 2
        else:
            i += 1

    return combinations


print(part_one(adapters.copy()))
print(part_two(adapters.copy()))
