from utils import read_split, timed

import heapq


elf_cals = [sum([-int(c) for c in elf.split('\n')]) for elf in read_split('day01.txt', '\n\n')]
heapq.heapify(elf_cals)

@timed
def part_one(elf_cals):
    return -heapq.heappop(elf_cals)

@timed
def part_two(elf_cals):
    return sum(-heapq.heappop(elf_cals) for _ in range(3))


print(part_one(elf_cals.copy()))
print(part_two(elf_cals.copy()))
