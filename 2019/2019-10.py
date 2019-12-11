from utils import timed

@timed
def part_one():
    asteroid_map = open('inputs/2019-10.txt').read().splitlines()

    asteroids = []
    for y, row in enumerate(asteroid_map):
        for x, column in enumerate(row):
            if column == '#':
                asteroids.append((x, y))

    visible_list = []
    for a in asteroids:
        visible = set()
        for other in asteroids:
            if other != a:
                try:
                    slope = (other[1] - a[1]) / (other[0] - a[0])
                except ZeroDivisionError:
                    slope = None
                direction = ''
                if other[0] < a[0]:
                    direction += 'L'
                elif other[0] > a[0]:
                    direction += 'R'
                if other[1] < a[1]:
                    direction += 'U'
                elif other[1] > a[1]:
                    direction += 'D'
                visible.add((slope, direction))
        visible_list.append(len(visible))

    print(max(visible_list))

    return asteroids, asteroids[visible_list.index(max(visible_list))]

@timed
def part_two(asteroids, bms):
    asteroids.remove(bms)
    asteroid_info = []
    for a in asteroids:
        try:
            slope = (a[1] - bms[1]) / (a[0] - bms[0])
        except ZeroDivisionError:
            slope = None
        direction = ''
        if a[0] < bms[0]:
            direction += 'L'
        elif a[0] > bms[0]:
            direction += 'R'
        if a[1] < bms[1]:
            direction += 'U'
        elif a[1] > bms[1]:
            direction += 'D'
        distance = abs(a[0] - bms[0]) + abs((a[1] - bms[1]))
        asteroid_info.append((slope, direction, distance, a))

    order = ('U', 'RU', 'R', 'RD', 'D', 'LD', 'L', 'LU')

    sorted_asteroids = []
    for i in range(8):
        to_append = [a for a in asteroid_info if a[1] == order[i]]
        if len(order[i]) == 2:
            # This SHOULD be reverse=True, but apparently a line going up and right has a negative slope
            # I mean the program works so I don't wanna fix this in case it breaks
            to_append = sorted(to_append, key=lambda a: a[0])
        sorted_asteroids += to_append

    vaporized_asteroid_count = 0
    non_vaporized_asteroids = sorted_asteroids.copy()
    while vaporized_asteroid_count < 200:
        vaporized_slopes = []
        for a in sorted_asteroids:
            if a not in non_vaporized_asteroids or a[:2] in vaporized_slopes:
                continue

            same_slope = [a]
            for other in non_vaporized_asteroids:
                if other != a:
                    if other[0] == a[0] and other[1] == a[1]:
                        same_slope.append(other)
            same_slope.sort(key=lambda a: a[2])
            vaporized_asteroid_count += 1
            if vaporized_asteroid_count == 200:
                print(same_slope[0][3][0] * 100 + same_slope[0][3][1])
                break
            else:
                non_vaporized_asteroids.remove(same_slope[0])
                vaporized_slopes.append(same_slope[0][:2])


# bms = best monitoring station
asteroids, bms = part_one()
part_two(asteroids, bms)
