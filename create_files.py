import sys

with open('sample_file.py.example') as f:
    contents = f.read()

with open(f'{sys.argv[1]}/day{sys.argv[2].zfill(2)}.py', 'w+') as f:
    f.write(contents)

with open(f'{sys.argv[1]}/inputs/day{sys.argv[2].zfill(2)}.txt', 'w') as f:
    pass
