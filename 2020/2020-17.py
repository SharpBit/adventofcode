import itertools

from utils import timed

with open('inputs/2020-17.txt') as f:
    z_layer_0 = [list(row) for row in f.read().splitlines()]

def create_pd(z_layer_0, dimensions):
    pd = {}
    for y, col in enumerate(z_layer_0):
        for x, cube in enumerate(col):
            pd[tuple([x - 1, y - 1] + [0] * (dimensions - 2))] = cube

    return pd

def extend_pd(pd, axis_ranges):
    upd_axis_ranges = []
    for axis in axis_ranges:
        upd_axis_ranges.append([axis[0] - 1, axis[1] + 1])

    for x in range(*upd_axis_ranges[0]):
        for y in range(*upd_axis_ranges[1]):
            for z in range(*upd_axis_ranges[2]):
                if len(upd_axis_ranges) == 4:
                    for w in range(*upd_axis_ranges[3]):
                        if pd.get((x, y, z, w)) is None:
                            pd[(x, y, z, w)] = '.'
                else:
                    if pd.get((x, y, z)) is None:
                        pd[(x, y, z)] = '.'

    return pd, upd_axis_ranges

def get_adjacent_cubes(cycle_layout, mutable_layout, coords, dimensions):
    adjustments = [adj for adj in itertools.product([-1, 0, 1], repeat=dimensions) if adj != tuple([0] * dimensions)]

    adj_cubes = []
    for adj in adjustments:
        upd_coords = []
        for axis, axis_adj in zip(coords, adj):
            upd_coords.append(axis + axis_adj)
        try:
            adj_cubes.append(cycle_layout[tuple(upd_coords)])
        except KeyError:
            mutable_layout[tuple(upd_coords)] = '.'
            adj_cubes.append('.')

    return adj_cubes

def cycle_pocket_dimension(z_layer_0, num_cycles, num_dimensions):
    pd = create_pd(z_layer_0, num_dimensions)
    axis_ranges = [[-1, len(z_layer_0) - 1], [-1, len(z_layer_0) - 1]] + [[0, 1]] * (num_dimensions - 2)
    for _ in range(num_cycles):
        pd, axis_ranges = extend_pd(pd, axis_ranges)
        cycle_layout = pd.copy()
        for coords, cube_state in cycle_layout.items():
            adj_cubes = get_adjacent_cubes(cycle_layout, pd, coords, num_dimensions)

            if cube_state == '#' and adj_cubes.count('#') not in (2, 3):
                pd[coords] = '.'
            elif cube_state == '.' and adj_cubes.count('#') == 3:
                pd[coords] = '#'

    return list(pd.values()).count('#')

@timed
def part_one(z_layer_0):
    return cycle_pocket_dimension(z_layer_0, 6, 3)

@timed
def part_two(z_layer_0):
    return cycle_pocket_dimension(z_layer_0, 6, 4)


print(part_one(z_layer_0))
print(part_two(z_layer_0))
