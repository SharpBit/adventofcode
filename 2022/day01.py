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
def part_one(elf_cals):
    heapq.heapify(elf_cals)
    return -heapq.heappop(elf_cals)

@timed
def part_two(elf_cals):
    heapq.heapify(elf_cals)
    return sum(-heapq.heappop(elf_cals) for _ in range(3))


print(part_one(elf_cals.copy()))
print(part_two(elf_cals.copy()))
