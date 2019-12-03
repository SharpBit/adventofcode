from utils import timed

# Wow, this one was hard.
# https://adventofcode.com/2018/day/2

# Part 1
@timed
def part_one():
    box_ids = open('inputs/2018-02.txt').read().split('\n')

    times = []
    for b in box_ids:
        counts = dict((b.count(letter), letter) for letter in b)
        times.append((1 if counts.get(2) else 0, 1 if counts.get(3) else 0))
    print(sum([x[0] for x in times]) * sum(x[1] for x in times))

# Part 2

@timed
def part_two():
    box_ids = open('inputs/2018-02.txt').read().split('\n')

    for x in box_ids:
        for y in box_ids:
            diff = 0
            index = 0
            for i, j in enumerate(x):
                if y[i] != j:
                    diff += 1
                    index = i
            if diff == 1:
                print(y[:index] + y[index + 1:])
                return


part_one()
part_two()
