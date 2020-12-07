from utils import timed

# day 7 part 2 was a nightmare, just like last year's...

with open('inputs/2020-07.txt') as f:
    input_lines = f.read().splitlines()

def find_parent_bags(rules, color):
    possible_parent_bags = []
    for outer_bag, inner_bags in rules.items():
        if color in inner_bags.keys():
            possible_parent_bags.append(outer_bag)

    return possible_parent_bags + sum([find_parent_bags(rules, outer_bag) for outer_bag in possible_parent_bags], [])

@timed
def part_one(input_lines):
    rules = {}
    for rule in input_lines:
        child_bags = ' '.join(rule.split(' ')[4:]).split(', ')
        outer_bag = ' '.join(rule.split(' ')[:2])
        child_bags_dict = {}
        for bag in child_bags:
            split_bag = bag.split(' ')
            if split_bag[0] == 'no':
                break
            child_bags_dict[' '.join(split_bag[1:3]).strip('.')] = int(split_bag[0])
        rules[outer_bag] = child_bags_dict

    return rules, len(set(find_parent_bags(rules, 'shiny gold')))

def product(array: list) -> int:
    res = 1
    for i in array:
        res *= i
    return res

def get_num_child_bags(rules, color, parent_bags_numlist):
    if len(rules[color]) == 0:
        return 0  # no more layers left, no more additional bags to add

    total_bag_counts = []
    for bag, count in rules[color].items():
        branch_count_list = parent_bags_numlist.copy()  # duplicate the count list for the current branch
        current_layer_sum = count * product(branch_count_list)

        branch_count_list.append(count)  # add this layer's count to the parent numlist for future layers
        future_layer_sum = get_num_child_bags(rules, bag, branch_count_list)
        total_bag_counts.append(current_layer_sum + future_layer_sum)

    return sum(total_bag_counts)

@timed
def part_two(rules):
    return get_num_child_bags(rules, 'shiny gold', [1])


rules, answer = part_one(input_lines)
print(answer)
print(part_two(rules))
