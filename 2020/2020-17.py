import itertools

from utils import timed

with open('inputs/2020-17.txt') as f:
    z_layer_0 = [list(row) for row in f.read().splitlines()]

def get_adjacent_cubes(cycle_layout, mutable_layout, x, y, z):
    adjustments = set(itertools.combinations([-1, 0, 1] * 3, 3))
    adjustments.remove((0, 0, 0))

    adj_cubes = []
    for x_adj, y_adj, z_adj in adjustments:
        try:
            adj_cubes.append(cycle_layout[(x + x_adj, y + y_adj, z + z_adj)])
        except KeyError:
            mutable_layout[(x + x_adj, y + y_adj, z + z_adj)] = '.'
            adj_cubes.append('.')

    return adj_cubes

def create_pd(z_layer_0):
    pd = {}
    for y, col in enumerate(z_layer_0):
        for x, cube in enumerate(col):
            pd[(x - 1, y - 1, 0)] = cube

    return pd

def extend_pd(pd, axis_ranges):
    for i in range(len(axis_ranges)):
        axis_ranges[i][0] -= 1
        axis_ranges[i][1] += 1

    for x in range(*axis_ranges[0]):
        for y in range(*axis_ranges[1]):
            for z in range(*axis_ranges[2]):
                if pd.get((x, y, z)) is None:
                    pd[(x, y, z)] = '.'

    return pd, axis_ranges

@timed
def part_one(z_layer_0):
    pd = create_pd(z_layer_0)
    # The range has to be
    axis_ranges = [[-1, len(z_layer_0[0]) - 1], [-1, len(z_layer_0) - 1], [0, 1]]
    for _ in range(6):
        pd, axis_ranges = extend_pd(pd, axis_ranges)
        cycle_layout = pd.copy()
        for coords, cube_state in cycle_layout.items():
            adj_cubes = get_adjacent_cubes(cycle_layout, pd, *coords)
            if cube_state == '#' and adj_cubes.count('#') not in (2, 3):
                pd[coords] = '.'
            elif cube_state == '.' and adj_cubes.count('#') == 3:
                pd[coords] = '#'

    return list(pd.values()).count('#')


print(part_one(z_layer_0))
