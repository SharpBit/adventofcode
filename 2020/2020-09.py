from utils import timed

with open('inputs/2020-09.txt') as f:
    data_stream = list(map(int, f.read().splitlines()))

@timed
def part_one(data_stream):
    preamble_length = 25
    for i, num in enumerate(data_stream[preamble_length:]):
        preamble = data_stream[i:i + preamble_length]
        acceptable_nums = [x + y for j, x in enumerate(preamble) for y in preamble[j + 1:]]
        if num not in acceptable_nums:
            return num

    raise Exception('no invalid number')

@timed
def part_two(data_stream, invalid_num):
    stream_length = 2
    while True:
        contiguous_lists = []
        for i in range(len(data_stream) - (stream_length - 1)):
            contiguous_lists.append([data_stream[i + j] for j in range(0, stream_length)])

        for possibility in contiguous_lists:
            if sum(possibility) == invalid_num:
                return min(possibility) + max(possibility)

        stream_length += 1


invalid_num = part_one(data_stream)
print(invalid_num)
print(part_two(data_stream, invalid_num))
