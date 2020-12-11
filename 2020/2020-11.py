from utils import timed

with open('inputs/2020-11.txt') as f:
    seat_layout = [list(row) for row in f.read().splitlines()]

def get_adjacent_seats(layout_dict, row, column):
    seats = []
    adjustments = [
        (-1, -1),  # Top left
        (-1, 0),  # Top
        (-1, 1),  # Top right
        (0, -1),  # Left
        (0, 1),  # Right
        (1, -1),  # Bottom left
        (1, 0),  # Bottom
        (1, 1)  # Bottom right
    ]
    for row_adj, col_adj in adjustments:
        try:
            seats.append(layout_dict[(row + row_adj, column + col_adj)])
        except KeyError:
            pass

    return seats

def save_seats(seat_layout):
    layout_dict = {}
    for i, row in enumerate(seat_layout):
        for j, seat in enumerate(row):
            layout_dict[(i, j)] = seat

    return layout_dict

@timed
def part_one(seat_layout):
    layout_dict = save_seats(seat_layout)
    while True:
        round_layout = layout_dict.copy()
        for (row, col), seat in round_layout.items():
            if seat == '.':
                continue

            adj_seats = get_adjacent_seats(round_layout, row, col)

            if seat == 'L' and adj_seats.count('#') == 0:
                layout_dict[(row, col)] = '#'
            elif seat == '#' and adj_seats.count('#') >= 4:
                layout_dict[(row, col)] = 'L'

        if round_layout == layout_dict:
            return list(layout_dict.values()).count('#')

def get_closest_seats(layout_dict, row, column):
    """An adaptation of get_adjacent_seats"""
    seats = []
    adjustments = [
        (-1, -1),  # Top left
        (-1, 0),  # Top
        (-1, 1),  # Top right
        (0, -1),  # Left
        (0, 1),  # Right
        (1, -1),  # Bottom left
        (1, 0),  # Bottom
        (1, 1)  # Bottom right
    ]
    for i, (row_adj, col_adj) in enumerate(adjustments):
        try:
            seat = '.'
            while seat == '.':
                seat = layout_dict[(row + row_adj, column + col_adj)]
                row_adj += adjustments[i][0]
                col_adj += adjustments[i][1]
            seats.append(seat)
        except KeyError:
            pass

    return seats

@timed
def part_two(seat_layout):
    layout_dict = save_seats(seat_layout)
    while True:
        round_layout = layout_dict.copy()
        for (row, col), seat in round_layout.items():
            if seat == '.':
                continue

            adj_seats = get_closest_seats(round_layout, row, col)

            if seat == 'L' and adj_seats.count('#') == 0:
                layout_dict[(row, col)] = '#'
            elif seat == '#' and adj_seats.count('#') >= 5:
                layout_dict[(row, col)] = 'L'

        if round_layout == layout_dict:
            return list(layout_dict.values()).count('#')


print(part_one(seat_layout))
print(part_two(seat_layout))
