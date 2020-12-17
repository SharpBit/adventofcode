from utils import timed

import itertools

with open('inputs/2020-11.txt') as f:
    seat_layout = [list(row) for row in f.read().splitlines()]

def save_seats(seat_layout):
    layout_dict = {}
    for i, row in enumerate(seat_layout):
        for j, seat in enumerate(row):
            layout_dict[(i, j)] = seat

    return layout_dict

def get_adjacent_seats(layout_dict, row, col):
    seats = []
    adjustments = [adj for adj in itertools.product([-1, 0, 1], repeat=2) if adj != (0, 0)]

    for row_adj, col_adj in adjustments:
        try:
            seats.append(layout_dict[(row + row_adj, col + col_adj)])
        except KeyError:
            pass

    return seats

@timed
def part_one(seat_layout):
    layout_dict = save_seats(seat_layout)
    while True:
        round_layout = layout_dict.copy()
        for coords, seat in round_layout.items():
            if seat == '.':
                continue

            adj_seats = get_adjacent_seats(round_layout, *coords)

            if seat == 'L' and adj_seats.count('#') == 0:
                layout_dict[coords] = '#'
            elif seat == '#' and adj_seats.count('#') >= 4:
                layout_dict[coords] = 'L'

        if round_layout == layout_dict:
            return list(layout_dict.values()).count('#')

def get_closest_seats(layout_dict, row, col):
    """An adaptation of get_adjacent_seats"""
    seats = []
    adjustments = [adj for adj in itertools.product([-1, 0, 1], repeat=2) if adj != (0, 0)]
    for i, (row_adj, col_adj) in enumerate(adjustments):
        try:
            seat = '.'
            while seat == '.':
                seat = layout_dict[(row + row_adj, col + col_adj)]
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
        for coords, seat in round_layout.items():
            if seat == '.':
                continue

            adj_seats = get_closest_seats(round_layout, *coords)

            if seat == 'L' and adj_seats.count('#') == 0:
                layout_dict[coords] = '#'
            elif seat == '#' and adj_seats.count('#') >= 5:
                layout_dict[coords] = 'L'

        if round_layout == layout_dict:
            return list(layout_dict.values()).count('#')


print(part_one(seat_layout))
print(part_two(seat_layout))
