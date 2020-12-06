from utils import timed

with open('inputs/2020-06.txt') as f:
    input_lines = f.read().splitlines()

def get_group_indexes(input_lines):
    group_indexes = []
    for i, line in enumerate(input_lines):
        if i == 0 or input_lines[i - 1] == '':  # beginning of a group
            group_indexes.append([i, None])
        if i == len(input_lines) - 1 or input_lines[i + 1] == '':  # end of a group
            group_indexes[-1][1] = i

    return group_indexes

@timed
def part_one(input_lines):
    group_indexes = get_group_indexes(input_lines)
    return sum([len(set(''.join(input_lines[group_index[0]:group_index[1] + 1]))) for group_index in group_indexes])

@timed
def part_two(input_lines):
    group_indexes = get_group_indexes(input_lines)

    unique_yes_answers = []
    for group_index in group_indexes:
        group_responses = input_lines[group_index[0]:group_index[1] + 1]
        responses_to_check = {letter: True for letter in group_responses[0]}

        for g in group_responses[1:]:
            for letter in responses_to_check.keys():
                if letter not in g:
                    responses_to_check[letter] = False

        unique_yes_answers.append(len([i for i in responses_to_check.values() if i]))

    return sum(unique_yes_answers)


print(part_one(input_lines))
print(part_two(input_lines))
