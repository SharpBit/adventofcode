from utils import timed

# I think I might give up today
# Comment about 2 hours after this: Part 1 was easy, Part 2 took way longer than it should have
# https://adventofcode.com/2018/day/3

# Part 1
import re


fabric = [[0 for i in range(1000)] for i in range(1000)]
claims = [i for i in open('2018-3.txt').read().split('\n')]


@timed
def part_one():
    global fabric
    global claims

    for c in claims:
        cd = re.findall(r'\#[0-9]+ \@ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', c)
        from_left = int(cd[0][0])
        from_top = int(cd[0][1])
        width = int(cd[0][2])
        height = int(cd[0][3])

        for i in range(from_left, from_left + width):
            for j in range(from_top, from_top + height):
                fabric[i][j] += 1

    overlapping = sum(1 for i in fabric for j in i if j >= 2)
    print(overlapping)

# Part 2

@timed
def part_two():
    global fabric
    global claims
    for c in claims:
        cd = re.findall(r'\#([0-9]+) \@ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', c)
        case_num = int(cd[0][0])
        from_left = int(cd[0][1])
        from_top = int(cd[0][2])
        width = int(cd[0][3])
        height = int(cd[0][4])
        p = True
        for i in range(from_left, from_left + width):
            for j in range(from_top, from_top + height):
                if fabric[i][j] != 1:
                    p = False
                    break # makes it faster
            if not p:
                break # makes it faster
        if p:
            print(case_num)


part_one()
part_two()
