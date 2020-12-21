from sympy.ntheory.modular import crt  # sympy is a module that does Chinese remainder theorem for you

from utils import timed

with open('inputs/2020-13.txt') as f:
    lines = f.read().splitlines()
    earliest_time = int(lines[0])
    buses = [int(b) if b != 'x' else b for b in lines[1].split(',')]

@timed
def part_one(earliest_time, buses):
    buses = [b for b in buses if isinstance(b, int)]
    times_to_wait = {b - earliest_time % b: b for b in buses}
    min_wait = min(list(times_to_wait.keys()))
    return min_wait * times_to_wait[min_wait]

@timed
def part_two(buses):
    # tbh i have no clue how crt works I just know that it must be used over brute force
    bus_dict = {}
    for i, b in enumerate(buses):
        if b != 'x':
            if i == 0:
                bus_dict[b] = i
            else:
                bus_dict[b] = b - i
    return min(crt(list(bus_dict.keys()), list(bus_dict.values())))

    # My original bruteforce solution ;-;
    # Now that I know the actual solution, I can estimate that this solution would take about 523 days to complete
    multiple = int(1e14 / buses[0])  # the question said the answer is larger than 10^14
    while True:
        target_num = buses[0] * multiple
        for i, b in enumerate(buses):
            if isinstance(b, int) and i != 0:
                if b - target_num % b != i:
                    break
        else:
            return target_num

        multiple += 1


print(part_one(earliest_time, buses))
print(part_two(buses))
