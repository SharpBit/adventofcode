import regex as re  # Pip package called regex that makes it easy to find overlapping matches

from utils import timed

with open('inputs/2020-20.txt') as f:
    lines = f.read().splitlines()

    tiles = {}
    i = 0
    while i < len(lines):
        tile_id = re.match(r'Tile (\d+):', lines[i]).group(1)
        tiles[int(tile_id)] = lines[i + 1:i + lines.index('')]
        i += lines.index('') + 1


@timed
def part_one(tiles):
    tile_borders = {}
    for tile_id, tile in tiles.items():
        borders = [
            tile[0],
            tile[-1],
            ''.join([row[0] for row in tile]),
            ''.join([row[-1] for row in tile])
        ]
        for border in borders:
            if tile_borders.get(border):
                tile_borders[border].append(tile_id)
            elif tile_borders.get(border[::-1]):
                tile_borders[border[::-1]].append(tile_id)
            else:
                tile_borders[border] = [tile_id]

    edge_tiles = [tile_id[0] for tile_id in tile_borders.values() if len(tile_id) == 1]
    corner_tiles = []
    product = 1
    for tile_id in edge_tiles:
        if edge_tiles.count(tile_id) == 2 and tile_id not in corner_tiles:
            corner_tiles.append(tile_id)
            product *= tile_id

    return product, tile_borders, corner_tiles

def rotate_tile(tile, deg):
    for _ in range(int(deg / 90)):
        cols = [''.join([row[i] for row in tile]) for i in range(len(tile[0]))]
        tile = [c[::-1] for c in cols]
    return tile

def flip_tile(tile, direction):
    """direction=0 is horizontal, direction=1 is vertical"""
    if direction == 0:
        return [row[::-1] for row in tile]
    return tile[::-1]

def create_orientation_list(tile):
    possible_orientations = []
    for r in range(4):
        rtile = rotate_tile(tile, r * 90)
        possible_orientations.append(rtile)
        for f in range(2):
            possible_orientations.append(flip_tile(rtile, f))

    return possible_orientations

def find_other_item(lst, item):
    for i in lst:
        if i != item:
            return i

def orient_next_tile(tiles, tiles_to_left, tiles_to_top, tile_id, first_col_id):
    try:
        left_tile = tiles_to_left[-1]
        right_border = ''.join([row[-1] for row in left_tile])
    except IndexError:
        left_tile = None
        first_col_id = tile_id
    try:
        top_tile = tiles_to_top[len(tiles_to_left)]
        bot_border = top_tile[-1]
    except IndexError:
        top_tile = None

    current_tile = tiles[tile_id]
    possible_orientations = create_orientation_list(current_tile)

    for o in possible_orientations:
        num_correct = 0
        if left_tile:
            if ''.join([row[0] for row in o]) == right_border:
                num_correct += 1
        else:
            num_correct += 1
        if top_tile:
            if o[0] == bot_border:
                num_correct += 1
        else:
            num_correct += 1

        if num_correct == 2:
            tiles_to_left.append(o)
            break

    ctile_borders = {border: tile_ids for border, tile_ids in tile_borders.items() if len(tile_ids) == 2 and tile_id in tile_ids}
    if len(tiles_to_left) == 12:
        left_row_tile = tiles_to_left[0]
        lrt_bot_border = left_row_tile[-1]

        try:
            next_tile_id = find_other_item(tile_borders[lrt_bot_border], first_col_id)
        except KeyError:
            next_tile_id = find_other_item(tile_borders[lrt_bot_border[::-1]], first_col_id)

        tiles_to_top = tiles_to_left
        tiles_to_left = []
    else:
        try:
            next_tile_id = find_other_item(ctile_borders[''.join([row[-1] for row in tiles_to_left[-1]])], tile_id)
        except KeyError:
            try:
                next_tile_id = find_other_item(ctile_borders[''.join([row[-1] for row in tiles_to_left[-1]])[::-1]], tile_id)
            except KeyError:
                next_tile_id = None

    try:
        prev_tile = tiles_to_left[-1]
    except IndexError:
        prev_tile = tiles_to_top[-1]

    if next_tile_id:
        return prev_tile + orient_next_tile(tiles, tiles_to_left, tiles_to_top, next_tile_id, first_col_id)

    return prev_tile


@timed
def part_two(tiles, tile_borders, corner_tiles):
    corner_id = corner_tiles[0]
    corner_tile = tiles[corner_id]
    possible_orientations = create_orientation_list(corner_tile)
    ctile_borders = {border: tile_ids for border, tile_ids in tile_borders.items() if len(tile_ids) == 2 and corner_id in tile_ids}

    for o in possible_orientations:
        num_correct = 0
        for border in ctile_borders.keys():
            bottom_and_right = (o[-1], ''.join([row[-1] for row in o]))
            if border in bottom_and_right:
                num_correct += 1
            elif border[::-1] in bottom_and_right:
                num_correct += 1
        if num_correct == 2:
            top_left_tile = o
            break

    try:

        next_tile_id = find_other_item(ctile_borders[''.join([row[-1] for row in top_left_tile])], corner_id)
    except KeyError:
        next_tile_id = find_other_item(ctile_borders[''.join([row[-1] for row in top_left_tile])[::-1]], corner_id)


    # Returns a list of all the rows, every 10 rows is 1 tile
    flat_image_rows = orient_next_tile(
        tiles=tiles,
        tiles_to_left=[top_left_tile],
        tiles_to_top=[],
        tile_id=next_tile_id,
        first_col_id=corner_id
    )

    i = 0
    flat_image = [top_left_tile]
    while i < len(flat_image_rows):
        flat_image.append(flat_image_rows[i:i + 10])
        i += 10

    # Remove borders
    for i in range(len(flat_image)):
        flat_image[i] = [row[1:-1] for row in flat_image[i][1:-1]]


    i = 0
    image_arr = []
    while i < len(flat_image):
        image_arr.append(flat_image[i:i + 12])
        i += 12

    image = []
    for img_row in image_arr:
        row_fmt = ['' for _ in range(8)]
        for tile in img_row:
            for i, tile_row in enumerate(tile):
                row_fmt[i] += tile_row
        image += row_fmt

    image_possibilities = create_orientation_list(image)
    for p in image_possibilities:
        p_str = '\n'.join(p)
        match = re.findall(r'#[#\.\n]{78}#[#\.]{4}##[#\.]{4}##[#\.]{4}###[#\.\n]{78}#[#\.]{2}#[#\.]{2}#[#\.]{2}#[#\.]{2}#[#\.]{2}#', p_str, overlapped=True)
        if len(match) > 0:
            return p_str.count('#') - len(match) * 15


answer, tile_borders, corner_tiles = part_one(tiles)
print(answer)
print(part_two(tiles, tile_borders, corner_tiles))
