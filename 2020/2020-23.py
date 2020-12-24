from utils import timed

with open('inputs/2020-23.txt') as f:
    cups = [int(c) for c in f.read()]

def mix_cups(cups, first_cup, moves):
    for i in range(moves):
        if i == 0:
            current_cup = first_cup
        else:
            current_cup = cups[current_cup]

        # Remove 3 cups clockwise from the current cup
        removed_cup1 = cups[current_cup]
        removed_cup2 = cups[removed_cup1]
        removed_cup3 = cups[removed_cup2]
        cups[current_cup] = cups[removed_cup3]
        del cups[removed_cup1]
        del cups[removed_cup2]
        del cups[removed_cup3]

        destination_cup = current_cup - 1
        lowest_cup = 1
        # Using == instead of in to hopefully save time
        while lowest_cup == removed_cup1 or lowest_cup == removed_cup2 or lowest_cup == removed_cup3:
            lowest_cup += 1

        while (destination_cup == removed_cup1 or destination_cup == removed_cup2
               or destination_cup == removed_cup3 or destination_cup < lowest_cup):  # noqa: W503
            destination_cup -= 1
            if destination_cup < lowest_cup:
                destination_cup = len(cups) + 3

        cups[removed_cup3] = cups[destination_cup]
        cups[removed_cup2] = removed_cup3
        cups[removed_cup1] = removed_cup2
        cups[destination_cup] = removed_cup1

    return cups

@timed
def part_one(cups):
    first_cup = cups[0]
    cups = {c: cups[i + 1] if i != len(cups) - 1 else cups[0] for i, c in enumerate(cups)}
    cups = mix_cups(cups, first_cup, 100)
    sequence = []
    next_cup = cups[1]
    while next_cup != 1:
        sequence.append(str(next_cup))
        next_cup = cups[next_cup]
    return ''.join(sequence)

@timed
def part_two(cups):
    # Takes about 15-17 seconds
    first_cup = cups[0]
    original_cups = {c: cups[i + 1] if i != len(cups) - 1 else 10 for i, c in enumerate(cups)}
    other_cups = {i: i + 1 if i != 1_000_000 else cups[0] for i in range(10, 1_000_001)}
    cups = {**original_cups, **other_cups}
    cups = mix_cups(cups, first_cup, 10_000_000)
    return cups[1] * cups[cups[1]]


print(part_one(cups))
print(part_two(cups))
