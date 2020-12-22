from utils import timed

with open('inputs/2020-21.txt') as f:
    all_ingredients = []
    all_allergens = []
    for food_item in f.read().splitlines():
        food_info = food_item.split(' ')
        all_ingredients.append(food_info[:food_info.index('(contains')])
        all_allergens.append([a.strip('),') for a in food_info[food_info.index('(contains') + 1:]])

def intersect_lists(lists):
    intersected = lists[0]
    for lst in lists[1:]:
        intersected_copy = intersected.copy()
        for item in intersected:
            if item not in lst:
                intersected_copy.remove(item)

        intersected = intersected_copy.copy()

    return intersected

@timed
def part_one(all_ingredients, all_allergens):
    allergen_dict = {}
    for allergen in set([a for food_alg in all_allergens for a in food_alg]):
        allergen_dict[allergen] = []
        for ings, allergens in zip(all_ingredients, all_allergens):
            if allergen in allergens:
                allergen_dict[allergen].append(ings)

    allergen_ings = {allergen: intersect_lists(ings) for allergen, ings in allergen_dict.items()}

    flat_ingredients = [ing for food_ing in all_ingredients for ing in food_ing]
    # Maybe I should actually write down what each variable's structure is so i dont compare a string w/ a list...
    # and spend 1 hour wondering why it doesnt work
    safe_ingredients = [ing for ing in flat_ingredients if ing not in [a for pa in allergen_ings.values() for a in pa]]
    return len(safe_ingredients), allergen_ings

@timed
def part_two(allergen_ings):
    allergen_iter_order = sorted([a for a in allergen_ings.keys()], key=lambda a: len(allergen_ings[a]))
    allergen2ingredient_map = {}
    removed_ingredients = []
    while len(allergen2ingredient_map) < len(allergen_iter_order):
        for a in allergen_iter_order:
            if len(allergen_ings[a]) == 1:
                allergen2ingredient_map[a] = allergen_ings[a][0]
                removed_ingredients.append(allergen_ings[a][0])
            else:
                for ing in removed_ingredients:
                    if ing in allergen_ings[a]:
                        allergen_ings[a].remove(ing)

    alphasorted_allergens = sorted(allergen2ingredient_map.keys())
    output = ''
    for a in alphasorted_allergens:
        output += f'{allergen2ingredient_map[a]},'
    return output[:-1]


answer, allergen_ings = part_one(all_ingredients, all_allergens)
print(answer)
print(part_two(allergen_ings))
