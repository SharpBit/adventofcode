from utils import timed

with open('inputs/2020-03.txt') as f:
    rows = list(map(lambda r: r.strip(), f.readlines()))  # get rid of newline chars

def find_num_trees(row_increment, col_increment):
    row = 0
    column = 0
    trees = 0
    while row < len(rows) - 1:
        row += row_increment
        column += col_increment
        if rows[row][column % len(rows[row])] == '#':
            trees += 1

    return trees

@timed
def part_one():
    return find_num_trees(1, 3)

@timed
def part_two():
    fnt = find_num_trees
    slopes = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))

    num_trees_list = [fnt(*slope) for slope in slopes]
    product = 1
    for result in num_trees_list:
        product *= result
    return product


print(part_one())
print(part_two())
