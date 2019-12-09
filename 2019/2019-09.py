from utils import timed


class elist(list):
    """A list that appends a default value to the list if the index is past the list length"""

    def __init__(self, r=list(), default=0):
        list.__init__(self, r)
        self.default = default

    def __getitem__(self, n):
        while len(self) <= n:
            self.append(self.default)
        return super().__getitem__(n)

    def __setitem__(self, n, d):
        while len(self) <= n:
            self.append(self.default)
        super().__setitem__(n, d)

    def copy(self):
        return elist(r=self, default=self.default)


class IntcodeSolver:
    def __init__(self, intcode):
        self.intcode = intcode.copy()
        self.pointer = 0
        self.output = None
        self.base = 0
        self.increments = (4, 4, 2, 2, 3, 3, 4, 4, 2)

    def get_param(self, mode, n, save=False):
        if mode == 0:
            val = self.intcode[self.pointer + n]
        elif mode == 1:
            if save is True:
                raise ValueError(f'Save index at {self.pointer + n} is in immediate mode')
            val = self.pointer + n
        elif mode == 2:
            val = self.base + self.intcode[self.pointer + n]

        return self.intcode[val] if save is False else val

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
                self.intcode[self.get_param(modes[2], 3, save=True)] = self.get_param(modes[0], 1) + self.get_param(modes[1], 2)
            elif opcode == 2:
                self.intcode[self.get_param(modes[2], 3, save=True)] = self.get_param(modes[0], 1) * self.get_param(modes[1], 2)
            elif opcode == 3:
                if not inputs:
                    return self.output, True
                self.intcode[self.get_param(modes[0], 1, save=True)] = inputs.pop(0)
            elif opcode == 4:
                self.output = self.get_param(modes[0], 1)
            elif opcode == 5:
                if self.get_param(modes[0], 1) != 0:
                    self.pointer = self.get_param(modes[1], 2) - 3
            elif opcode == 6:
                if self.get_param(modes[0], 1) == 0:
                    self.pointer = self.get_param(modes[1], 2) - 3
            elif opcode == 7:
                self.intcode[self.get_param(modes[2], 3, save=True)] = int(self.get_param(modes[0], 1) < self.get_param(modes[1], 2))
            elif opcode == 8:
                self.intcode[self.get_param(modes[2], 3, save=True)] = int(self.get_param(modes[0], 1) == self.get_param(modes[1], 2))
            elif opcode == 9:
                self.base += self.get_param(modes[0], 1)
            elif opcode == 99:
                return self.output, False
            else:
                raise ValueError(f'Unknown opcode {opcode} at index {self.pointer}')

            self.pointer += self.increments[opcode - 1]


@timed
def part_one():
    intcode = elist(r=[int(x) for x in open('inputs/2019-09.txt').read().split(',')])
    output, _ = IntcodeSolver(intcode).run(1)
    print(output)

@timed
def part_two():
    intcode = elist(r=[int(x) for x in open('inputs/2019-09.txt').read().split(',')])
    output, _ = IntcodeSolver(intcode).run(2)
    print(output)


part_one()
part_two()
