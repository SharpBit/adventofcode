from collections import defaultdict

from utils import read_lines, timed

grid = [list(map(int, line)) for line in read_lines('day08.txt')]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited = defaultdict(set)
def is_visible(row, col, dr, dc, height):
    '''This can be iterative, but initially I thought this was like the pacific/atlantic
    water flow leetcode question so I thought I needed to dfs, and I'm not going to rewrite it'''
    if (row, col) in visited[(dr, dc)]:
        return True
    if row + dr not in range(len(grid)) or col + dc not in range(len(grid[0])):
        visited[(dr, dc)].add((row, col))
        return True
    if height > grid[row + dr][col + dc]:
        return is_visible(row + dr, col + dc, dr, dc, height)
    return False


@timed
def part_one():
    visible = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for dr, dc in directions:
                if is_visible(r, c, dr, dc, grid[r][c]):
                    visible.add((r, c))
                    break
    return len(visible)

@timed
def part_two():
    highest_score = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            score = 1
            for dr, dc in directions:
                dist = 0
                while True:
                    row = r + (dist + 1) * dr
                    col = c + (dist + 1) * dc
                    if row not in range(len(grid)) or col not in range(len(grid[0])):
                        score *= dist
                        break
                    dist += 1
                    if grid[row][col] >= grid[r][c]:
                        score *= dist
                        break
                if score == 0:
                    break
            highest_score = max(score, highest_score)

    return highest_score


print(part_one())
print(part_two())
