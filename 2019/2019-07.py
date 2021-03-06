import itertools

from utils import timed


class IntcodeSolver:
    def __init__(self, intcode):
        self.intcode = intcode.copy()
        self.pointer = 0
        self.output = None
        self.increments = (4, 4, 2, 2, 3, 3, 4, 4)

    def get_param(self, mode, n):
        if mode == 0:
            return self.intcode[self.intcode[self.pointer + n]]
        elif mode == 1:
            return self.intcode[self.pointer + n]

    def run(self, inputs):
        """Returns output[int], is_running[bool]"""
        # Part 2 only passes in 1 input
        if type(inputs) == int:
            inputs = [inputs]

        while True:
            instruction = f'{self.intcode[self.pointer]:05}'
            opcode = int(instruction[-2:])
            modes = [int(m) for m in reversed(instruction[:3])]

            if opcode == 1:
                self.intcode[self.intcode[self.pointer + 3]] = self.get_param(modes[0], 1) + self.get_param(modes[1], 2)
            elif opcode == 2:
                self.intcode[self.intcode[self.pointer + 3]] = self.get_param(modes[0], 1) * self.get_param(modes[1], 2)
            elif opcode == 3:
                if not inputs:
                    return self.output, True
                self.intcode[self.intcode[self.pointer + 1]] = inputs.pop(0)
            elif opcode == 4:
                self.output = self.get_param(modes[0], 1)
            elif opcode == 5:
                if self.get_param(modes[0], 1) != 0:
                    self.pointer = self.get_param(modes[1], 2) - 3
            elif opcode == 6:
                if self.get_param(modes[0], 1) == 0:
                    self.pointer = self.get_param(modes[1], 2) - 3
            elif opcode == 7:
                self.intcode[self.intcode[self.pointer + 3]] = int(self.get_param(modes[0], 1) < self.get_param(modes[1], 2))
            elif opcode == 8:
                self.intcode[self.intcode[self.pointer + 3]] = int(self.get_param(modes[0], 1) == self.get_param(modes[1], 2))
            elif opcode == 99:
                return self.output, False
            else:
                raise ValueError(f'Unknown opcode {opcode} at index {self.pointer}')

            self.pointer += self.increments[opcode - 1]


@timed
def part_one():
    intcode = [int(x) for x in open('inputs/2019-07.txt').read().split(',')]
    combos = []
    for p in itertools.permutations(range(5)):
        output = 0
        for i in range(5):
            output, _ = IntcodeSolver(intcode).run([p[i], output])
        combos.append(output)
    print(max(combos))

@timed
def part_two():
    intcode = [int(x) for x in open('inputs/2019-07.txt').read().split(',')]
    combos = []
    for p in itertools.permutations(range(5, 10)):
        amps = []
        last_output = 0
        is_running = True
        for i in range(5):
            amps.append(IntcodeSolver(intcode))
            amps[i].run(p[i])
        while is_running:
            for i, a in enumerate(amps):
                last_output, is_running = a.run(last_output)
        combos.append(last_output)
    print(max(combos))


part_one()
part_two()
