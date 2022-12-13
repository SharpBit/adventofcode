from functools import cmp_to_key
from itertools import zip_longest

from utils import read_split, timed

packet_pairs = [list(eval(p) for p in pair.split('\n')) for pair in read_split('day13.txt', '\n\n')]

def compare(l1: list, l2: list) -> int:
    '''Compares two lists. Returns -1, 0, or 1 so we can use cmp_to_key'''
    for left, right in zip_longest(l1, l2):
        if left is None:
            return -1
        if right is None:
            return 1
        if type(left) == int and type(right) == int:
            if left < right:
                return -1
            if left > right:
                return 1
        else:
            if type(left) == int:
                left = [left]
            if type(right) == int:
                right = [right]
            res = compare(left, right)
            if res != 0:
                return res
    return 0

@timed
def part_one():
    return sum(i + 1 for i, pair in enumerate(packet_pairs) if compare(*pair) == -1)

@timed
def part_two():
    packets = [p for pair in packet_pairs for p in pair]
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(compare))
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


print(part_one())
print(part_two())
