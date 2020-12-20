from utils import timed

import re


with open('inputs/2020-19.txt') as f:
    lines = f.read().splitlines()
    rules = lines[:lines.index('')]
    msgs = lines[lines.index('') + 1:]


def parse_rules(rules, part):
    rules_dict = {}
    for r in rules:
        if part == 2:
            if r == '8: 42':
                r = '8: 42 | 42 8'
            elif r == '11: 42 31':
                r = '11: 42 31 | 42 11 31'
        rule_num, required_match = r.split(': ')
        parsed_match = []
        if '"' in required_match:
            parsed_match.append([required_match.strip('"')])
        else:
            matches = required_match.split(' | ')
            for match in matches:
                parsed_match.append(list(map(int, match.split(' '))))

        rules_dict[int(rule_num)] = parsed_match

    return rules_dict


REPEATED_RECURSION = 0

def get_rule_pattern(rules, num):
    global REPEATED_RECURSION
    options = []
    for option in rules[num]:
        match = []
        for sub_rule in option:
            if sub_rule in ('a', 'b'):
                match.append(sub_rule)
            else:
                if sub_rule == num:
                    REPEATED_RECURSION += 1
                if REPEATED_RECURSION > 5:  # This can be adjusted until the output stops changing or the recursion limit gets hit
                    match.append('')
                    REPEATED_RECURSION = 0
                else:
                    match.append(get_rule_pattern(rules, sub_rule))


        options.append(''.join(match))

    if len(options) == 1:
        return fr'{options[0]}'
    return fr"({'|'.join(options)})"

@timed
def part_one(rules, msgs):
    rules = parse_rules(rules, 1)
    re_pattern = get_rule_pattern(rules, 0)

    valid_msgs = 0
    for msg in msgs:
        if re.fullmatch(re_pattern, msg):
            valid_msgs += 1

    return valid_msgs

@timed
def part_two(rules, msgs):
    rules = parse_rules(rules, 2)
    re_pattern = get_rule_pattern(rules, 0)

    valid_msgs = 0
    for msg in msgs:
        if re.fullmatch(re_pattern, msg):
            valid_msgs += 1

    return valid_msgs


print(part_one(rules, msgs))
print(part_two(rules, msgs))
