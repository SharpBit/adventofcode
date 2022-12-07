from utils import read_lines, timed


games = [tuple(g.split(' ')) for g in read_lines('day02.txt')]
# rps
# abc
# xyz

@timed
def part_one():
    score = 0
    for g in games:
        opp_move = ord(g[0]) - ord('A')
        your_move = ord(g[1]) - ord('X')
        score += (your_move - opp_move + 1) % 3 * 3
        score += your_move + 1
    return score

@timed
def part_two():
    score = 0
    for g in games:
        opp_move = ord(g[0]) - ord('A')
        outcome = ord(g[1]) - ord('X')
        score += outcome % 3 * 3
        score += ((outcome + opp_move - 1) % 3) + 1
    return score


print(part_one())
print(part_two())
