from utils import timed

with open('inputs/2020-25.txt') as f:
    public_keys = list(map(int, f.read().splitlines()))

@timed
def part_one(public_keys):
    subject_num = 7
    value = 1
    loop_size = 1
    public_keys.sort()
    while True:
        value *= subject_num
        value %= 20201227
        if value == public_keys[0]:
            break
        loop_size += 1

    subject_num = public_keys[1]
    value = 1
    for _ in range(loop_size):
        value *= subject_num
        value %= 20201227

    return value


print(part_one(public_keys))
