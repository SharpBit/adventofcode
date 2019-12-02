from utils import timed
# https://adventofcode.com/2019/day/2
# The hard part for this one was understanding the problem, the coding part was easy

@timed
def part_one():
    with open('2019-2.txt') as f:
        intcode = list(map(int, f.read().split(',')))

    # Part of puzzle prompt
    intcode[1] = 12
    intcode[2] = 2

    opcode = None
    opcode_index = 0
    while True:
        opcode = intcode[opcode_index]
        if opcode == 99:
            break
        if opcode == 1:
            intcode[intcode[opcode_index + 3]] = intcode[intcode[opcode_index + 1]] + intcode[intcode[opcode_index + 2]]
        elif opcode == 2:
            intcode[intcode[opcode_index + 3]] = intcode[intcode[opcode_index + 1]] * intcode[intcode[opcode_index + 2]]
        else:
            print(f'Unknown opcode {opcode}')

        opcode_index += 4

    print(intcode[0])


@timed
def part_two():
    with open('2019-2.txt') as f:
        intcode = list(map(int, f.read().split(',')))

    for noun in range(100):
        for verb in range(100):
            test_input = intcode.copy()
            test_input[1] = noun
            test_input[2] = verb

            opcode = None
            opcode_index = 0
            while True:
                opcode = test_input[opcode_index]
                if opcode == 99:
                    break
                if opcode == 1:
                    test_input[test_input[opcode_index + 3]] = test_input[test_input[opcode_index + 1]] + test_input[test_input[opcode_index + 2]]
                elif opcode == 2:
                    test_input[test_input[opcode_index + 3]] = test_input[test_input[opcode_index + 1]] * test_input[test_input[opcode_index + 2]]
                else:
                    print(f'Unknown opcode {opcode}')

                opcode_index += 4

            if test_input[0] == 19690720:
                print(100 * noun + verb)


part_one()
part_two()