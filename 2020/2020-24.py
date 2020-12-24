from utils import timed

import re

with open('inputs/2020-24.txt') as f:
    nondelim_tiles = f.read().splitlines()
    tiles = [re.findall(r'(e|se|sw|w|nw|ne)', t) for t in nondelim_tiles]

# Cube coordinates
adjustments = {
    'ne': (1, 0, -1),
    'sw': (-1, 0, 1),
    'se': (0, -1, 1),
    'nw': (0, 1, -1),
    'e': (1, -1, 0),
    'w': (-1, 1, 0)
}

@timed
def part_one(tiles):
    tile_colors = {}

    for steps in tiles:
        coords = [0, 0, 0]
        for s in steps:
            coords = [c + a for a, c in zip(coords, adjustments[s])]

        current_color = tile_colors.get(tuple(coords), False)
        tile_colors[tuple(coords)] = not current_color

    return len([c for c in tile_colors.values() if c]), tile_colors

def get_adj_colors(tile_colors, coords):
    black = 0
    for adj in adjustments.values():
        color = tile_colors.get(tuple([c + a for a, c in zip(coords, adj)]), False)
        if color:
            black += 1

    return black

def add_adj_colors(tile_colors):
    color_copy = tile_colors.copy()
    for coords in tile_colors.keys():
        for adj in adjustments.values():
            adj_coords = tuple([c + a for a, c in zip(coords, adj)])
            adj_tile = color_copy.get(adj_coords)
            if adj_tile is None:
                color_copy[adj_coords] = False

    return color_copy

@timed
def part_two(tile_colors):
    # Takes ~15 seconds to run
    for i in range(100):
        tile_colors = add_adj_colors(tile_colors)
        tiles_to_flip = []
        for coords, color in tile_colors.items():
            black = get_adj_colors(tile_colors, coords)
            if (color is True and (black == 0 or black > 2)) or (color is False and black == 2):
                tiles_to_flip.append(coords)

        for coords in tiles_to_flip:
            tile_colors[coords] = not tile_colors[coords]

    return len([c for c in tile_colors.values() if c])


answer, tile_colors = part_one(tiles)
print(answer)
print(part_two(tile_colors))
