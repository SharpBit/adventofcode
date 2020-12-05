from utils import timed

with open('inputs/2020-05.txt') as f:
    boarding_passes = f.read().splitlines()

def partition_binary_space(min_num: int, max_num: int, lower_symbol: str, upper_symbol: str, sequence: str) -> int:
    for i in sequence:
        if i == lower_symbol:
            max_num -= int((max_num - min_num) / 2) + 1
        elif i == upper_symbol:
            min_num += int((max_num - min_num) / 2) + 1
        else:
            raise ValueError(f'Incorrect symbol {i}')

    if min_num != max_num:
        raise ValueError('Incorrect sequence length or min/max number')

    return min_num

@timed
def part_one(boarding_passes):
    seat_ids = []
    for bp in boarding_passes:
        row_num = partition_binary_space(0, 127, 'F', 'B', bp[:7])
        col_num = partition_binary_space(0, 7, 'L', 'R', bp[7:])
        seat_ids.append(row_num * 8 + col_num)

    return seat_ids

@timed
def part_two(seat_ids):
    seat_ids.sort()
    previous_seat_id = -1
    for seat in seat_ids:
        if previous_seat_id != -1 and seat - 1 != previous_seat_id:
            return seat - 1
        previous_seat_id = seat


# Part 1
seat_ids = part_one(boarding_passes)
print(max(seat_ids))
# Part 2
print(part_two(seat_ids))
