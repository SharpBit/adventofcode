from utils import timed
from typing import List, Tuple
# the explanation of order of inputs for part 2 took forever to understand

def solve_intcode(intcode: List[int], input_values: List[int], pointer: int=0) -> Tuple[int, List[int], int, bool]:
    input_index = 0
    output = None
    halted = False

    opcode = None
    while True:
        opcode = f'{intcode[pointer]:05}'

        if opcode[-2:] == '99':
            halted = True
            break
        if opcode[-2:] == '01':
            save_index = intcode[pointer + 3]
            first_num = intcode[pointer + 1] if opcode[-3] == '0' else pointer + 1
            second_num = intcode[pointer + 2] if opcode[-4] == '0' else pointer + 2
            intcode[save_index] = intcode[first_num] + intcode[second_num]
            pointer += 4
        elif opcode[-2:] == '02':
            save_index = intcode[pointer + 3]
            first_num = intcode[pointer + 1] if opcode[-3] == '0' else pointer + 1
            second_num = intcode[pointer + 2] if opcode[-4] == '0' else pointer + 2
            intcode[save_index] = intcode[first_num] * intcode[second_num]
            pointer += 4
        elif opcode[-2:] == '03':
            save_index = intcode[pointer + 1]
            try:
                intcode[save_index] = input_values[input_index]
            except IndexError:
                return output, intcode, pointer, halted
            input_index += 1
            pointer += 2
        elif opcode[-2:] == '04':
            index = intcode[pointer + 1] if opcode[-3] == '0' else pointer + 1
            output = intcode[index]
            pointer += 2
        elif opcode[-2:] == '05':
            check_index = intcode[pointer + 1] if opcode[-3] == '0' else pointer + 1
            set_index = intcode[pointer + 2] if opcode[-4] == '0' else pointer + 2
            if intcode[check_index] != 0:
                pointer = intcode[set_index]
            else:
                pointer += 3
        elif opcode[-2:] == '06':
            check_index = intcode[pointer + 1] if opcode[-3] == '0' else pointer + 1
            set_index = intcode[pointer + 2] if opcode[-4] == '0' else pointer + 2
            if intcode[check_index] == 0:
                pointer = intcode[set_index]
            else:
                pointer += 3
        elif opcode[-2:] == '07':
            first_index = intcode[pointer + 1] if opcode[-3] == '0' else pointer + 1
            second_index = intcode[pointer + 2] if opcode[-4] == '0' else pointer + 2
            if intcode[first_index] < intcode[second_index]:
                intcode[intcode[pointer + 3]] = 1
            else:
                intcode[intcode[pointer + 3]] = 0
            pointer += 4
        elif opcode[-2:] == '08':
            first_index = intcode[pointer + 1] if opcode[-3] == '0' else pointer + 1
            second_index = intcode[pointer + 2] if opcode[-4] == '0' else pointer + 2
            if intcode[first_index] == intcode[second_index]:
                intcode[intcode[pointer + 3]] = 1
            else:
                intcode[intcode[pointer + 3]] = 0
            pointer += 4
        else:
            raise ValueError(f'Unknown opcode {opcode} in index {pointer}')

    return output, intcode, pointer, halted

@timed
def part_one():
    intcode = [int(x) for x in open('inputs/2019-07.txt').read().split(',')]
    combos = []
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    for e in range(5):
                        if len(set([a, b, c, d, e])) < 5:
                            continue
                        intcode_copy = intcode.copy()
                        amp_a, *_ = solve_intcode(intcode_copy, [a, 0])
                        intcode_copy = intcode.copy()
                        amp_b, *_ = solve_intcode(intcode_copy, [b, amp_a])
                        intcode_copy = intcode.copy()
                        amp_c, *_ = solve_intcode(intcode_copy, [c, amp_b])
                        intcode_copy = intcode.copy()
                        amp_d, *_ = solve_intcode(intcode_copy, [d, amp_c])
                        intcode_copy = intcode.copy()
                        amp_e, *_ = solve_intcode(intcode_copy, [e, amp_d])

                        combos.append(int(amp_e))

    print(max(combos))

@timed
def part_two():
    intcode = [int(x) for x in open('inputs/2019-07.txt').read().split(',')]
    combos = []
    for a in range(5, 10):
        for b in range(5, 10):
            for c in range(5, 10):
                for d in range(5, 10):
                    for e in range(5, 10):
                        if len(set([a, b, c, d, e])) < 5:
                            continue

                        intcode_a = intcode.copy()
                        intcode_b = intcode.copy()
                        intcode_c = intcode.copy()
                        intcode_d = intcode.copy()
                        intcode_e = intcode.copy()

                        loop = 0
                        halted = False
                        while not halted:
                            if loop == 0:
                                amp_a, intcode_a, pointer_a, _ = solve_intcode(intcode_a, [a])
                                amp_b, intcode_b, pointer_b, _ = solve_intcode(intcode_b, [b])
                                amp_c, intcode_c, pointer_c, _ = solve_intcode(intcode_c, [c])
                                amp_d, intcode_d, pointer_d, _ = solve_intcode(intcode_d, [d])
                                amp_e, intcode_e, pointer_e, halted = solve_intcode(intcode_e, [e])
                                amp_e = 0
                            else:
                                amp_a, intcode_a, pointer_a, _ = solve_intcode(intcode_a, [amp_e], pointer=pointer_a)
                                amp_b, intcode_b, pointer_b, _ = solve_intcode(intcode_b, [amp_a], pointer=pointer_b)
                                amp_c, intcode_c, pointer_c, _ = solve_intcode(intcode_c, [amp_b], pointer=pointer_c)
                                amp_d, intcode_d, pointer_d, _ = solve_intcode(intcode_d, [amp_c], pointer=pointer_d)
                                amp_e, intcode_e, pointer_e, halted = solve_intcode(intcode_e, [amp_d], pointer=pointer_e)

                            loop += 1

                        combos.append(int(amp_e))

    print(max(combos))


part_one()
part_two()
