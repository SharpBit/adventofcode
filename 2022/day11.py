import heapq
import math
import re

from copy import deepcopy

from utils import read_split, timed


class Monkey:
    def __init__(self, lines):
        item_match = re.search(r'\s+Starting items: (.+)', lines[1])
        assert item_match
        if item_match:
            self.items = list(map(int, item_match.group(1).split(', ')))

        op_match = re.search(r'\s+Operation: new = old (.) (.+)', lines[2])
        assert op_match
        if op_match:
            # Tried to do this with lambda funcs but for some reason all the lambda funcs became
            # the last monkey's function even though they were different mem addresses so this will have to do
            self.op, self.op_num = op_match.groups()

        divide_match = re.search(r'\s+Test: divisible by (\d+)', lines[3])
        assert divide_match
        if divide_match:
            self.divisible_test = int(divide_match.group(1))

        self.pass_test = int(lines[4][-1])
        self.fail_test = int(lines[5][-1])
        self.inspections = 0

    def __lt__(self, other):
        '''Greater than for a max heap'''
        return self.inspections > other.inspections

    def __repr__(self):
        return f'Monkey<{self.items=} {self.op=} {self.op_num=} {self.divisible_test=}' \
            f' {self.pass_test=} {self.fail_test=} {self.inspections=}'


monkeys = [Monkey(m.split('\n')) for m in read_split('day11.txt', '\n\n')]

@timed
def part_one(monkeys):
    for _ in range(20):
        for m in monkeys:
            for worry_lvl in m.items:
                m.inspections += 1
                num2 = worry_lvl if m.op_num == 'old' else int(m.op_num)
                if m.op == '+':
                    worry_lvl += num2
                else:
                    worry_lvl *= num2
                worry_lvl = worry_lvl // 3
                if worry_lvl % m.divisible_test == 0:
                    monkeys[m.pass_test].items.append(worry_lvl)
                else:
                    monkeys[m.fail_test].items.append(worry_lvl)
            m.items.clear()

    heapq.heapify(monkeys)
    return heapq.heappop(monkeys).inspections * heapq.heappop(monkeys).inspections

@timed
def part_two(monkeys):
    lcm = math.lcm(*[m.divisible_test for m in monkeys])
    for _ in range(10_000):
        for m in monkeys:
            for worry_lvl in m.items:
                m.inspections += 1
                num2 = worry_lvl if m.op_num == 'old' else int(m.op_num)
                if m.op == '+':
                    worry_lvl += num2
                else:
                    worry_lvl *= num2
                worry_lvl %= lcm  # kinda cheated for this but it's a math thing so...
                if worry_lvl % m.divisible_test == 0:
                    monkeys[m.pass_test].items.append(worry_lvl)
                else:
                    monkeys[m.fail_test].items.append(worry_lvl)
            m.items.clear()

    heapq.heapify(monkeys)
    return heapq.heappop(monkeys).inspections * heapq.heappop(monkeys).inspections


print(part_one(deepcopy(monkeys)))
print(part_two(deepcopy(monkeys)))
