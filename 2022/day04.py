from utils import timed

import re

pairs = []
with open('inputs/day04.txt') as f:
    for pair in f.readlines():
        match = re.search(r'(\d+)-(\d+),(\d+)-(\d+).*', pair)
        pairs.append(tuple(map(int, match.groups())))

@timed
def part_one():
    return sum(1 for pair in pairs if (pair[0] >= pair[2] and pair[1] <= pair[3]) or (pair[0] <= pair[2] and pair[1] >= pair[3]))

@timed
def part_two():
    return sum(1 for pair in pairs if (pair[0] >= pair[2] and pair[0] <= pair[3]) or (pair[2] >= pair[0] and pair[2] <= pair[1]))


print(part_one())
print(part_two())
