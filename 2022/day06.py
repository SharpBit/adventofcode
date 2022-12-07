from utils import timed


stream = open('inputs/day06.txt').read().strip()

@timed
def part_one():
    for i in range(len(stream)):
        if len(set(stream[i:i + 4])) == 4:
            return i + 4

@timed
def part_two():
    for i in range(len(stream)):
        if len(set(stream[i:i + 14])) == 14:
            return i + 14


print(part_one())
print(part_two())
