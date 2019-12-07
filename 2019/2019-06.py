from utils import timed


@timed
def part_one():
    direct_orbits = {i.split(')')[1]: i.split(')')[0] for i in open('inputs/2019-06.txt').read().splitlines()}
    planets = set([p for p in direct_orbits.keys()] + [p for p in direct_orbits.values()])
    total_orbits = 0
    for p in planets:
        planet = p
        while planet != 'COM':
            total_orbits += 1
            planet = direct_orbits[planet]

    print(total_orbits)

@timed
def part_two():
    direct_orbits = {i.split(')')[1]: i.split(')')[0] for i in open('inputs/2019-06.txt').read().splitlines()}
    you_path = []
    santa_path = []

    p = 'YOU'
    while p != 'COM':
        you_path.append(direct_orbits[p])
        p = direct_orbits[p]

    p = 'SAN'
    while p != 'COM':
        santa_path.append(direct_orbits[p])
        p = direct_orbits[p]

    ecp = None
    for y in you_path:
        for s in santa_path:
            if y == s:
                ecp = y
                break
        if ecp:
            break
    print(you_path.index(ecp) + santa_path.index(ecp))  # Do not need to subtract 2 because index 0 is still 0 planets traveled


part_one()
part_two()
