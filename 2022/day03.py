from utils import read_lines, timed


sacks = [(set(s[:len(s) // 2]), set(s[len(s) // 2:])) for s in read_lines('day03.txt')]

def calc_prio(item):
    if item.isupper():
        return ord(item) - ord('A') + 27
    return ord(item) - ord('a') + 1

@timed
def part_one():
    prio = 0
    for c1, c2 in sacks:
        for item in c1:
            if item in c2:
                prio += calc_prio(item)
                break
    return prio

@timed
def part_two():
    prio = 0
    for i in range(0, len(sacks), 3):
        badge = (sacks[i][0] | sacks[i][1]) & (sacks[i + 1][0] | sacks[i + 1][1]) & (sacks[i + 2][0] | sacks[i + 2][1])
        for item in badge:  # should be only one
            prio += calc_prio(item)
    return prio


print(part_one())
print(part_two())
