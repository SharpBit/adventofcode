# https://adventofcode.com/2018/day/1
# Part 1
with open('2018-1.txt') as f:
    print(sum([int(i) for i in f.read().split('\n')]))

# Part 2
with open('2018-1.txt') as f:
    frequencies = [int(i) for i in f.read().split('\n')]

total = 0
prev = set()
found = False
while not found:
    for i in frequencies:
        total += i
        if total in prev:
            print(total)
            found = True
            break
        prev.add(total)
