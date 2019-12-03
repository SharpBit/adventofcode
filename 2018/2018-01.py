from utils import timed

# https://adventofcode.com/2018/day/1
# Part 1
@timed
def part_one():
    print(sum([int(i) for i in open('inputs/2018-01.txt').read().split('\n')]))

# Part 2

@timed
def part_two():
    frequencies = [int(i) for i in open('inputs/2018-01.txt').read().split('\n')]

    total = 0
    prev = set()
    found = False
    while not found:
        for i in frequencies:
            total += i
            if total in prev:
                print(total)
                found = True
                break
            prev.add(total)


part_one()
part_two()
