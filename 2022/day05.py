import re

from collections import deque
from copy import deepcopy

from utils import read_lines, timed


stacks = []
instructions = []

procedure = False
for line in read_lines('day05.txt'):
    if '[' not in line:
        procedure = True
    if not procedure:
        for i in range(0, len(line), 4):
            stack_num = int(i / 4)
            if stack_num >= len(stacks):
                stacks.append(deque())
            if line[i + 1] != ' ':
                stacks[stack_num].appendleft(line[i + 1])
    else:
        match = re.search(r'move (\d+) from (\d) to (\d).*', line)
        if match:
            instructions.append(tuple(map(int, match.groups())))

@timed
def part_one(stacks, instructions):
    for num, from_, to_ in instructions:
        for _ in range(num):
            stacks[to_ - 1].append(stacks[from_ - 1].pop())
    return ''.join(s[-1] for s in stacks)

@timed
def part_two(stacks, instructions):
    for num, from_, to_ in instructions:
        temp = [stacks[from_ - 1].pop() for _ in range(num)]
        for i in range(len(temp) - 1, -1, -1):
            stacks[to_ - 1].append(temp[i])
    return ''.join(s[-1] for s in stacks)


print(part_one(deepcopy(stacks), instructions))
print(part_two(deepcopy(stacks), instructions))
