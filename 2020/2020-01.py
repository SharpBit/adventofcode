from utils import timed

inputs = list(map(int, open('inputs/2020-01.txt').readlines()))

@timed
def part_one():
    for i, x in enumerate(inputs):
        for y in inputs[i + 1:]:
            if x + y == 2020:
                return x * y


print(part_one())

@timed
def part_two():
    for i, x in enumerate(inputs):
        for j, y in enumerate(inputs[i + 1:]):
            for z in inputs[j + 1:]:
                if x + y + z == 2020:
                    return x * y * z


print(part_two())
