from utils import timed


depths = [int(x) for x in open('inputs/2021-01.txt').readlines()]

@timed
def part_one():   
    return sum(1 for i, d in enumerate(depths) if d > depths[i - 1])

@timed
def part_two():
    sliding = [sum(depths[i:i + 3]) for i in range(len(depths))]
    return sum(1 for i, d in enumerate(sliding) if d > sliding[i - 1])


print(part_one())
print(part_two())
