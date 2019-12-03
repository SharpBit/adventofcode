from utils import timed

# https://adventofcode.com/2019/day/1

@timed
def part_one():
    print(sum(int(mass) // 3 - 2 for mass in open('inputs/2019-01.txt').readlines()))


def fuel_for_mass(mass):
    required_fuel = mass // 3 - 2
    if required_fuel <= 0:
        return 0
    return required_fuel + fuel_for_mass(required_fuel)


@timed
def part_two():
    print(sum(fuel_for_mass(int(mass)) for mass in open('inputs/2019-01.txt').readlines()))


part_one()
part_two()
