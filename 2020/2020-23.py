from utils import timed

with open('inputs/2020-23.txt') as f:
    cups = [int(c) for c in f.read()]

def mix_cups(cups, moves):
    cci = 0
    for i in range(moves):
        current_cup = cups[cci]
        removed_cups = []
        while len(removed_cups) < 3:
            try:
                removed_cups.append(cups.pop(cci + 1))
            except IndexError:
                removed_cups.append(cups.pop(0))

        destination_cup = current_cup - 1
        lowest_cup = 1
        while lowest_cup in removed_cups:
            lowest_cup += 1

        while destination_cup in removed_cups or destination_cup < lowest_cup:
            destination_cup -= 1
            if destination_cup < lowest_cup:
                destination_cup = len(cups) + 3
        insert_index = cups.index(destination_cup)
        cups = cups[:insert_index + 1] + removed_cups + cups[insert_index + 1:]
        cci = cups.index(current_cup) + 1
        if cci == len(cups):
            cci = 0

    return cups.index(1), cups

@timed
def part_one(cups):
    one_cup, cups = mix_cups(cups.copy(), 100)
    return ''.join([str(c) for c in cups[one_cup + 1:] + cups[:one_cup]])

@timed
def part_two(cups):
    one_cup, cups = mix_cups(cups + list(range(10, 1_000_001)), 10_000_000)
    try:
        return cups[one_cup + 1] * cups[one_cup + 2]
    except IndexError:
        return cups[one_cup + 1 - len(cups)] * cups[one_cup + 2 - len(cups)]


print(part_one(cups))
print(part_two(cups))
