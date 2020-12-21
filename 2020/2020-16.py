import re
from collections import Counter
from itertools import chain

from utils import timed

with open('inputs/2020-16.txt') as f:
    lines = f.read().splitlines()
    rule_matches = [list(re.match(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', line).groups()) for line in lines[:lines.index('')]]
    rules = {rule[0]: [int(r) if i % 2 == 0 else int(r) + 1 for i, r in enumerate(rule[1:])] for rule in rule_matches}

    your_ticket = list(map(int, lines[lines.index('') + 2].split(',')))
    nearby_tickets = [list(map(int, line.split(','))) for line in lines[lines.index('') + 5:]]

@timed
def part_one(rules, nearby_tickets):
    error_rate = 0
    for ticket in nearby_tickets:
        for field in ticket:
            for ranges in rules.values():
                if field in chain(range(*ranges[:2]), range(*ranges[2:])):
                    break
            else:
                error_rate += field
    return error_rate

@timed
def part_two(rules, nearby_tickets, your_ticket):
    valid_tickets = nearby_tickets.copy()
    for ticket in nearby_tickets:
        for field in ticket:
            for ranges in rules.values():
                if field in chain(range(*ranges[:2]), range(*ranges[2:])):
                    break
            else:
                valid_tickets.remove(ticket)


    valid_rule_fields = {k: [] for k in rules.keys()}
    for ticket in valid_tickets:
        for i, field in enumerate(ticket):
            for k, v in rules.items():
                if field in chain(range(*v[:2]), range(*v[2:])):
                    valid_rule_fields[k].append(i)  # adds to the list of possible fields for that rule


    counters = {k: [field for field, num_valid in Counter(v).items() if num_valid == len(valid_tickets)] for k, v in valid_rule_fields.items()}
    field_order = list(sorted(valid_rule_fields.keys(), key=lambda r: len(counters[r])))
    possible_fields = list(range(20))
    field_nums = {}
    for rule in field_order:
        for field in counters[rule]:
            if field in possible_fields:
                field_nums[rule] = field
                possible_fields.remove(field)
                break

    departure_fields = [f for f in rules.keys() if f.startswith('departure')]
    ans = 1
    for rule, field_index in field_nums.items():
        if rule in departure_fields:
            ans *= your_ticket[field_index]

    return ans


print(part_one(rules, nearby_tickets))
print(part_two(rules, nearby_tickets, your_ticket))
