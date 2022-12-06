from collections import deque

from utils import timed


stream = open('inputs/day06.txt').read().strip()

@timed
def part_one():
    marker = deque()
    for i, char in enumerate(stream):
        marker.append(char)
        if len(marker) > 4:
            marker.popleft()
        if len(set(marker)) == 4:
            return i + 1

@timed
def part_two():
    marker = deque()
    for i, char in enumerate(stream):
        marker.append(char)
        if len(marker) > 14:
            marker.popleft()
        if len(set(marker)) == 14:
            return i + 1


print(part_one())
print(part_two())
