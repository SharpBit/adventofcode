from utils import timed


with open('inputs/2020-18.txt') as f:
    problems = [list(p.replace(' ', '')) for p in f.read().splitlines()]

OPERATOR_MAP = {'+': int.__add__, '*': int.__mul__}

def get_corresponding_parenthesis(expr):
    istart = []  # stack of indices of opening parentheses

    for i, c in enumerate(expr):
        if c == '(':
            istart.append(i)
        if c == ')':
            istart.pop()
            if len(istart) == 0:
                return i

def evaluate(expr):
    i = 1
    try:
        total = int(expr[0])
    except ValueError:
        p_index = get_corresponding_parenthesis(expr)
        paren_expr = expr[i:p_index]
        total = evaluate(paren_expr)
        i = p_index + 1

    while i < len(expr):
        try:
            other = int(expr[i + 1])
        except ValueError:
            if expr[i + 1] == '(':
                p_index = get_corresponding_parenthesis(expr[i + 1:])
                paren_expr = expr[i + 2:i + p_index + 1]
                total = OPERATOR_MAP[expr[i]](total, evaluate(paren_expr))
                i = i + p_index + 2
            else:
                raise Exception(f'Something went wrong: next symbol is {expr[i + 1]}')
        else:
            total = OPERATOR_MAP[expr[i]](total, other)
            i += 2

    return total

@timed
def part_one(problems):
    return sum([evaluate(p) for p in problems])

class Rint(int):
    """An int class that reverses the order of operations"""
    def __add__(self, other):
        return Rint(int.__mul__(self, other))

    def __mul__(self, other):
        return Rint(int.__add__(self, other))

@timed
def part_two(problems):
    total_sum = 0
    for problem in problems:
        new_problem = ''
        for c in problem:
            if c.isdigit():
                new_problem += f'Rint({c})'
            elif c == '+':
                new_problem += '*'
            elif c == '*':
                new_problem += '+'
            else:
                # Parentheses
                new_problem += c

        total_sum += eval(new_problem)

    return total_sum


print(part_one(problems))
print(part_two(problems))
