from utils import timed

import copy
import re

with open('inputs/2020-08.txt') as f:
    instructions = f.read().splitlines()


class Program:
    SIGN_MAP = {'+': '__add__', '-': '__sub__'}

    def __init__(self, instructions):
        self.instructions = self.read_instructions(instructions) if isinstance(instructions[0], str) else instructions
        self.accumulator = 0
        self.index = 0
        self.executed_instructions = []

    def read_instructions(self, instructions):
        return [list(re.findall(r'(acc|jmp|nop) (\+|-)(\d+)', instruction)[0]) for instruction in instructions]

    def run(self) -> (int, bool):
        """
        Returns the accumulator when the program terminated/looped and whether or not the program terminated
        """
        while True:
            if self.index in self.executed_instructions:
                return self.accumulator, False

            try:
                opcode, sign, num = self.instructions[self.index]
            except IndexError:
                # Reached the end of the program for an instruction
                return self.accumulator, True

            num = int(num)
            self.executed_instructions.append(self.index)

            if opcode == 'acc':
                self.accumulator = getattr(self.accumulator, self.SIGN_MAP[sign])(num)
            elif opcode == 'jmp':
                self.index = getattr(self.index, self.SIGN_MAP[sign])(num) - 1
            elif opcode == 'nop':
                pass
            else:
                raise ValueError(f'Invalid opcode {opcode} in line {self.index + 1}')

            self.index += 1

    def create_instruction_possibilities(self):
        possible_instructions = []
        for i, (opcode, sign, num) in enumerate(self.instructions):
            if opcode == 'acc':
                continue

            instructions_copy = copy.deepcopy(self.instructions)
            instructions_copy[i][0] = 'jmp' if opcode == 'nop' else 'nop'
            possible_instructions.append(instructions_copy)

        return possible_instructions


@timed
def part_one(instructions):
    program = Program(instructions)
    accumulator, _ = program.run()
    return accumulator

@timed
def part_two(instructions):
    original_program = Program(instructions)
    possible_instructions = original_program.create_instruction_possibilities()

    for instructions in possible_instructions:
        program = Program(instructions)
        accumulator, terminated = program.run()
        if terminated:
            return accumulator

    raise Exception('No instruction reached the end of the program')


print(part_one(instructions))
print(part_two(instructions))
