from utils import timed
# https://adventofcode.com/2019/day/2
# The hard part for this one was understanding the problem, the coding part was easy

def solve_intcode(intcode, noun, verb):
    intcode[1] = noun
    intcode[2] = verb
    opcode = None
    for i in range(0, len(intcode), 4):
        opcode = intcode[i]
        if opcode == 99:
            break
        if opcode == 1:
            intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]
        elif opcode == 2:
            intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
        else:
            print(f'Unknown opcode {opcode}')

    return intcode[0]

@timed
def part_one():
    intcode = list(map(int, open('inputs/2019-02.txt').read().split(',')))
    print(solve_intcode(intcode, 12, 2))


@timed
def part_two():
    intcode = list(map(int, open('inputs/2019-02.txt').read().split(',')))

    for noun in range(100):
        for verb in range(100):
            test_input = intcode.copy()
            output = solve_intcode(test_input, noun, verb)
            if output == 19690720:
                print(100 * noun + verb)
                break


part_one()
part_two()