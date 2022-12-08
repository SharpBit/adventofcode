from utils import read_lines, timed

import heapq


class Directory:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.child_dirs = {}
        self.size = 0

    def add_child(self, dir_: 'Directory'):
        dir_.parent = self
        self.child_dirs[dir_.name] = dir_


root = Directory('/')
curr = root

for line in read_lines('day07.txt'):
    words = line.split(' ')
    if words[0] == '$' and words[1] == 'cd':
        if words[2] == '..':
            curr = curr.parent
        elif words[2] != '/':
            curr = curr.child_dirs[words[2]]
    elif words[0] == 'dir':
        curr.add_child(Directory(words[1]))
    elif words[0].isnumeric():
        curr.size += int(words[0])

dir_sizes = []

def dfs(root):
    total_size = root.size
    for child in root.child_dirs.values():
        total_size += dfs(child)
    dir_sizes.append(total_size)
    return total_size


@timed
def part_one():
    dfs(root)
    return sum(s for s in dir_sizes if s < 100_000)

@timed
def part_two():
    dir_sizes_local = dir_sizes.copy()
    free_space = 70_000_000 - dfs(root)
    min_delete = 30_000_000 - free_space
    heapq.heapify(dir_sizes_local)
    while len(dir_sizes_local) > 0:
        if (size := heapq.heappop(dir_sizes_local)) >= min_delete:
            return size


print(part_one())
print(part_two())
