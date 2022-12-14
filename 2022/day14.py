from utils import read_lines, timed

paths = [s.split(' -> ') for s in read_lines('day14.txt')]

lowest_y = 0
grid = {}
for p in paths:
    for i in range(1, len(p)):
        e1 = tuple(map(int, p[i - 1].split(',')))
        e2 = tuple(map(int, p[i].split(',')))
        for x in range(min(e1[0], e2[0]), max(e1[0], e2[0]) + 1):
            for y in range(min(e1[1], e2[1]), max(e1[1], e2[1]) + 1):
                grid[(x, y)] = '#'
                lowest_y = max(lowest_y, y)

@timed
def part_one(grid):
    grains = 0
    void = False
    while True:
        x = 500
        y = 0
        while True:
            if not grid.get((x, y + 1)):
                y += 1
            elif not grid.get((x - 1, y + 1)):
                x -= 1
                y += 1
            elif not grid.get((x + 1, y + 1)):
                x += 1
                y += 1
            else:
                grid[(x, y)] = 'o'
                grains += 1
                break
            if y >= lowest_y:
                void = True
                break
        if void:
            break

    return grains

@timed
def part_two(grid):
    grains = 0
    blocked = False
    while True:
        x = 500
        y = 0
        while True:
            if not grid.get((x, y + 1)):
                y += 1
            elif not grid.get((x - 1, y + 1)):
                x -= 1
                y += 1
            elif not grid.get((x + 1, y + 1)):
                x += 1
                y += 1
            else:
                grid[(x, y)] = 'o'
                grains += 1
                if x == 500 and y == 0:
                    blocked = True
                break
            if y == lowest_y + 1:
                grid[(x, y)] = 'o'
                grains += 1
                break
        if blocked:
            break

    return grains


print(part_one(grid.copy()))
print(part_two(grid.copy()))
