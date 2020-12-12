from utils import timed

with open('inputs/2020-12.txt') as f:
    actions = [(line[0], int(line[1:])) for line in f.read().splitlines()]

DIRECTION_MAP = {
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
    'N': (0, 1)
}

TURN_MAP = {'L': -1, 'R': 1}
ROTATE_MAP = {'L': 1, 'R': -1}  # Quadrants increase as you go counter-clockwise

@timed
def part_one(actions, direction):
    x = 0
    y = 0
    for action, num in actions:
        if action == 'F':
            action = direction
        if action in 'ESWN':
            x += DIRECTION_MAP[action][0] * num
            y += DIRECTION_MAP[action][1] * num
            continue

        index_inc = int(TURN_MAP[action] * (num / 90))
        direction_options = list(DIRECTION_MAP.keys())
        direction_map_index = direction_options.index(direction) + index_inc
        try:
            direction = direction_options[direction_map_index]
        except IndexError:
            direction = direction_options[direction_map_index % 4]

    return abs(x) + abs(y)

@timed
def part_two(actions, direction, waypoint_x, waypoint_y):
    ship_x = 0
    ship_y = 0
    for action, num in actions:
        if action == 'F':
            move_x = (waypoint_x - ship_x) * num
            move_y = (waypoint_y - ship_y) * num
            ship_x += move_x
            ship_y += move_y
            waypoint_x += move_x
            waypoint_y += move_y
        if action in 'ESWN':
            waypoint_x += DIRECTION_MAP[action][0] * num
            waypoint_y += DIRECTION_MAP[action][1] * num
            continue

        relative_coords = [waypoint_x - ship_x, waypoint_y - ship_y]

        times_rotate = int(num / 90)
        for i in range(times_rotate):
            if action == 'R':
                relative_coords = [relative_coords[1], -relative_coords[0]]
            elif action == 'L':
                relative_coords = [-relative_coords[1], relative_coords[0]]

        waypoint_x = ship_x + relative_coords[0]
        waypoint_y = ship_y + relative_coords[1]

    return abs(ship_x) + abs(ship_y)


print(part_one(actions, 'E'))
print(part_two(actions, 'E', 10, 1))
