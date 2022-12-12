from collections import deque

from utils import read_lines, timed

grid = []
possible_starts = []
for i, line in enumerate(read_lines('day12.txt')):
    for j, s in enumerate(line):
        if s == 'S':
            start = (i, j)
            possible_starts.append((i, j))
        elif s == 'E':
            end = (i, j)
        elif s == 'a':
            possible_starts.append((i, j))
    grid.append(list(line))

def bfs(start):
    curr = deque([start])
    next_ = deque()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()
    steps = 0
    while True:
        while curr:
            row, col = curr.popleft()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if r not in range(len(grid)) or \
                    c not in range(len(grid[0])) or \
                        (r, c) in visited:
                    continue
                if grid[row][col] in ('y', 'z') and grid[r][c] == 'E':
                    return steps + 1

                curr_elev = ord('a') if grid[row][col] == 'S' else ord(grid[row][col])
                if grid[r][c] == 'E':
                    next_elev = ord('z')
                elif grid[r][c] == 'S':
                    next_elev = ord('a')
                else:
                    next_elev = ord(grid[r][c])
                if next_elev - curr_elev <= 1:
                    next_.append((r, c))

        if not next_:
            break
        curr = next_.copy()
        next_.clear()
        steps += 1
    return float('inf')

@timed
def part_one():
    return bfs(start)

@timed
def part_two():
    return min(bfs(a) for a in possible_starts)


print(part_one())
print(part_two())
