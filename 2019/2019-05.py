from utils import timed

class IntcodeSolver:
    def __init__(self, intcode):
        self.intcode = intcode.copy()
        self.pointer = 0

    def get_param(self, mode, n):
        if mode == 0:
            return self.intcode[self.intcode[self.pointer + n]]
        elif mode == 1:
            return self.intcode[self.pointer + n]

    def run(self, given_input):
        while True:
            instruction = f'{self.intcode[self.pointer]:05}'
            opcode = int(instruction[-2:])
            modes = [int(m) for m in reversed(instruction[:3])]

            if opcode == 1:
                self.intcode[self.intcode[self.pointer + 3]] = self.get_param(modes[0], 1) + self.get_param(modes[1], 2)
                self.pointer += 4
            elif opcode == 2:
                self.intcode[self.intcode[self.pointer + 3]] = self.get_param(modes[0], 1) * self.get_param(modes[1], 2)
                self.pointer += 4
            elif opcode == 3:
                self.intcode[self.intcode[self.pointer + 1]] = given_input
                self.pointer += 2
            elif opcode == 4:
                output = self.get_param(modes[0], 1)
                print(output)
                self.pointer += 2
            elif opcode == 5:
                if self.get_param(modes[0], 1) != 0:
                    self.pointer = self.get_param(modes[1], 2)
                else:
                    self.pointer += 3
            elif opcode == 6:
                if self.get_param(modes[0], 1) == 0:
                    self.pointer = self.get_param(modes[1], 2)
                else:
                    self.pointer += 3
            elif opcode == 7:
                self.intcode[self.intcode[self.pointer + 3]] = int(self.get_param(modes[0], 1) < self.get_param(modes[1], 2))
                self.pointer += 4
            elif opcode == 8:
                self.intcode[self.intcode[self.pointer + 3]] = int(self.get_param(modes[0], 1) == self.get_param(modes[1], 2))
                self.pointer += 4
            elif opcode == 99:
                break
            else:
                print(f'Unknown opcode {opcode} at index {self.pointer}')

@timed
def part_one():
    intcode = [int(x) for x in open('inputs/2019-05.txt').read().split(',')]
    IntcodeSolver(intcode).run(1)

@timed
def part_two():
    intcode = [int(x) for x in open('inputs/2019-05.txt').read().split(',')]
    IntcodeSolver(intcode).run(5)


part_one()
part_two()
