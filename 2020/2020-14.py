from utils import timed

import itertools

import re

with open('inputs/2020-14.txt') as f:
    input_lines = f.read().splitlines()
    mask_subset = {}
    mask = ''
    memory_insertions = {}
    for line in input_lines:
        if line.startswith('mask'):
            if mask != '':
                mask_subset[mask] = memory_insertions
                memory_insertions = {}
            mask = line.split(' = ')[1]
        else:
            mem_addr, num = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
            memory_insertions[int(mem_addr)] = int(num)
    # The last mask never got added
    mask_subset[mask] = memory_insertions

@timed
def part_one(mask_subset):
    mem = {}
    for mask, mem_ins in mask_subset.items():
        for mem_addr, num in mem_ins.items():
            num_bin_digits = list(f'{num:036b}')
            for i, pos in enumerate(mask):
                if pos != 'X':
                    num_bin_digits[i] = pos
            mem[mem_addr] = int(''.join(num_bin_digits), 2)

    return sum(list(mem.values()))

@timed
def part_two(mask_subset):
    mem = {}
    for mask, mem_ins in mask_subset.items():
        for mem_addr, num in mem_ins.items():
            floating_digits = []
            mem_addr_bin_digits = list(f'{mem_addr:036b}')
            for i, pos in enumerate(mask):
                if pos == '1':
                    mem_addr_bin_digits[i] = pos
                elif pos == 'X':
                    floating_digits.append(i)

            mem_addrs = []
            # that lightbulb moment when u realize if u take every combo of the floating digits,
            # you end up with every possible binary number with that number of digits...
            possible_floating_combos = itertools.product(['0', '1'], repeat=len(floating_digits))
            for combo in possible_floating_combos:
                c = mem_addr_bin_digits.copy()
                for i, digit in enumerate(combo):
                    c[floating_digits[i]] = digit
                mem_addrs.append(c)


            for addr in mem_addrs:
                mem_addr = int(''.join(addr), 2)
                mem[mem_addr] = num

    return sum(list(mem.values()))


print(part_one(mask_subset))
print(part_two(mask_subset))
