from utils import read_lines, timed

mvts = [line.split(' ') for line in read_lines('day09.txt')]
dir_map = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

def sign(n):
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0

def sim_rope(num_knots):
    rope = [[0, 0] for _ in range(num_knots)]
    visited = set()
    for d, num in mvts:
        num = int(num)
        for _ in range(num):
            rope[0][0] = rope[0][0] + dir_map[d][0]
            rope[0][1] = rope[0][1] + dir_map[d][1]
            for i in range(1, len(rope)):
                x_dist = rope[i - 1][0] - rope[i][0]
                y_dist = rope[i - 1][1] - rope[i][1]

                if abs(x_dist) > 1 or abs(y_dist) > 1:
                    rope[i][0] = rope[i][0] + 1 * sign(x_dist)
                    rope[i][1] = rope[i][1] + 1 * sign(y_dist)
            visited.add(tuple(rope[-1]))

    return len(visited)

@timed
def part_one():
    return sim_rope(2)

@timed
def part_two():
    return sim_rope(10)


print(part_one())
print(part_two())
