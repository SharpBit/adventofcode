from utils import timed

# I started out trying a 2000x2000 grid for part 1 before realizing you needed to save line segments xD


def save_segments(instructions):
    segments = []
    last_segment = [[0, 0], [0, 0]]
    for i in instructions:
        direction = i[0]
        length = int(i[1:])
        if direction == 'R':
            last_point = last_segment[1]
            last_segment = [last_point, [last_point[0] + length, last_point[1]]]
            segments.append(last_segment)
        elif direction == 'L':
            last_point = last_segment[1]
            last_segment = [last_point, [last_point[0] - length, last_point[1]]]
            segments.append(last_segment)
        elif direction == 'U':
            last_point = last_segment[1]
            last_segment = [last_point, [last_point[0], last_point[1] + length]]
            segments.append(last_segment)
        elif direction == 'D':
            last_point = last_segment[1]
            last_segment = [last_point, [last_point[0], last_point[1] - length]]
            segments.append(last_segment)

    return segments

def find_intersections(wires):
    intersections = []
    for segment1 in wires[0]:
        for segment2 in wires[1]:
            if segment2[0][0] in range(*sorted((segment1[0][0], segment1[1][0]))) and segment1[0][1] in range(*sorted((segment2[0][1], segment2[1][1]))):
                intersections.append((segment2[0][0], segment1[0][1]))
            elif segment1[0][0] in range(*sorted((segment2[0][0], segment2[1][0]))) and segment2[0][1] in range(*sorted((segment1[0][1], segment1[1][1]))):
                intersections.append((segment1[0][0], segment2[0][1]))

    return intersections

@timed
def part_one():
    wires = [wire.split(',') for wire in open('inputs/2019-03.txt').readlines()]
    wire1 = save_segments(wires[0])
    wire2 = save_segments(wires[1])

    intersections = find_intersections([wire1, wire2])

    distances = [abs(x) + abs(y) for x, y in intersections]
    print(min(distances))


@timed
def part_two():
    wires = [wire.split(',') for wire in open('inputs/2019-03.txt').readlines()]
    wire1 = save_segments(wires[0])
    wire2 = save_segments(wires[1])

    intersections = find_intersections([wire1, wire2])

    intersection_steps = []
    for x, y in intersections:
        current_coords = [0, 0]
        x_key = dict(zip(['R', 'L', 'U', 'D'], [1, -1, 0, 0]))
        y_key = dict(zip(['R', 'L', 'U', 'D'], [0, 0, 1, -1]))

        steps = 0
        for instruction in wires[0]:
            direction = instruction[0]
            length = int(instruction[1:])

            for i in range(length):
                current_coords[0] += x_key[direction]
                current_coords[1] += y_key[direction]
                steps += 1
                if current_coords[0] == x and current_coords[1] == y:
                    break
            if current_coords[0] == x and current_coords[1] == y:
                    break

        current_coords = [0, 0]
        for instruction in wires[1]:
            direction = instruction[0]
            length = int(instruction[1:])

            for i in range(length):
                current_coords[0] += x_key[direction]
                current_coords[1] += y_key[direction]
                steps += 1
                if current_coords[0] == x and current_coords[1] == y:
                    break
            if current_coords[0] == x and current_coords[1] == y:
                    break

        intersection_steps.append(steps)

    print(min(intersection_steps))


part_one()
part_two()
