from utils import timed

with open('inputs/2020-03.txt') as f:
    rows = list(map(lambda r: r.strip(), f.readlines()))  # get rid of newline chars

def find_num_trees(row_increment, col_increment):
    for i, row in enumerate(rows):
        rows[i] = row * int(len(rows) * col_increment / len(row) + 1)
    row = 0
    column = 0
    trees = 0
    while row < len(rows) - 1:
        row += row_increment
        column += col_increment
        if rows[row][column] == '#':
            trees += 1

    return trees

@timed
def part_one():
    return find_num_trees(1, 3)


@timed
def part_two():
    fnt = find_num_trees
    return fnt(1, 1) * fnt(1, 3) * fnt(1, 5) * fnt(1, 7) * fnt(2, 1)


print(part_one())
print(part_two())
