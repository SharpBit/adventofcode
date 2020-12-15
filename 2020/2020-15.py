from utils import timed

with open('inputs/2020-15.txt') as f:
    starting_nums = list(map(int, f.read().split(',')))

def calculate_spoken_num(sequence, index):
    spoken_index = len(sequence) + 1
    current_num = sequence[-1]
    sequence = {n: [i + 1] for i, n in enumerate(sequence)}
    while spoken_index <= index:
        if len(sequence[current_num]) == 1:
            # New number
            current_num = 0
        else:
            current_num = sequence[current_num][-1] - sequence[current_num][-2]

        try:
            sequence[current_num].append(spoken_index)
        except KeyError:
            sequence[current_num] = [spoken_index]

        spoken_index += 1


    return current_num

@timed
def part_one(sequence):
    return calculate_spoken_num(sequence, 2020)

@timed
def part_two(sequence):
    return calculate_spoken_num(sequence, 30_000_000)


print(part_one(starting_nums))
print(part_two(starting_nums))
