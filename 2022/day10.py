from utils import read_lines, timed

instructions = [line.split(' ') for line in read_lines('day10.txt')]

@timed
def part_one():
    cycle = 1
    i = 0
    skipped = False
    reg_x = 1
    signal_strengths = 0
    while i < len(instructions):
        if instructions[i][0] == 'addx' and not skipped:
            skipped = True
        elif instructions[i][0] == 'addx' and skipped:
            skipped = False
            reg_x += int(instructions[i][1])
            i += 1
        else:
            i += 1
        cycle += 1
        if cycle % 40 == 20:
            assert cycle <= 220
            signal_strengths += cycle * reg_x
    return signal_strengths

@timed
def part_two():
    cycle = 1
    i = 0
    skipped = False
    reg_x = 1
    output = ''
    while i < len(instructions):
        crt = (cycle - 1) % 40
        if abs(reg_x - crt) <= 1:
            output += '#'
        else:
            output += '.'
        if crt == 39:
            output += '\n'
        if instructions[i][0] == 'addx' and not skipped:
            skipped = True
        elif instructions[i][0] == 'addx' and skipped:
            skipped = False
            reg_x += int(instructions[i][1])
            i += 1
        else:
            i += 1
        cycle += 1
    return output


print(part_one())
print(part_two())
