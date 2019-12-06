from utils import timed
# Took almost 3 hours

def solve_intcode(intcode, given_input):
    opcode = None
    pointer = 0
    while True:
        opcode = f'{intcode[pointer]:05}'

        if opcode[-2:] == '99':
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
            intcode[save_index] = given_input
            pointer += 2
        elif opcode[-2:] == '04':
            index = intcode[pointer + 1] if opcode[-3] == '0' else pointer + 1
            output = intcode[index]
            print(output)
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
            print(f'Unknown opcode {opcode}')

@timed
def part_one():
    intcode = [int(x) for x in open('inputs/2019-05.txt').read().split(',')]
    solve_intcode(intcode, 1)

@timed
def part_two():
    intcode = [int(x) for x in open('inputs/2019-05.txt').read().split(',')]
    solve_intcode(intcode, 5)


part_one()
part_two()