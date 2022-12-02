from utils import timed

import heapq

elf_cals = []

with open('inputs/day01.txt') as f:
    total = 0
    for line in f.readlines():
        if line == '\n':
            elf_cals.append(-total)
            total = 0
        else:
            total += int(line)

@timed
def part_one():
    heapq.heapify(elf_cals)
    return -heapq.heappop(elf_cals)

@timed
def part_two():
    heapq.heapify(elf_cals)
    return sum(-heapq.heappop(elf_cals) for _ in range(2))


most_cals = part_one()
print(most_cals)
print(most_cals + part_two())
