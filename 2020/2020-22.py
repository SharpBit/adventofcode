from utils import timed

with open('inputs/2020-22.txt') as f:
    lines = f.read().splitlines()
    p1deck = list(map(int, lines[1:lines.index('')]))
    p2deck = list(map(int, lines[lines.index('') + 2:]))

@timed
def part_one(p1deck, p2deck):
    while len(p1deck) > 0 and len(p2deck) > 0:
        p1card = p1deck.pop(0)
        p2card = p2deck.pop(0)
        if p1card > p2card:
            p1deck.append(p1card)
            p1deck.append(p2card)
        else:
            p2deck.append(p2card)
            p2deck.append(p1card)

    winning_deck = p1deck if len(p2deck) == 0 else p2deck

    score = 0
    for i, card in enumerate(winning_deck[::-1]):
        score += card * (i + 1)

    return score

def play_rcombat_game(p1deck, p2deck) -> int:
    """Plays a recursive combat game and returns the player # of the winner"""
    previous_rounds = []
    while len(p1deck) > 0 and len(p2deck) > 0:
        previous_rounds.append([p1deck.copy(), p2deck.copy()])
        if [p1deck, p2deck] in previous_rounds[:-1]:
            p2deck = []
            break
        p1card = p1deck.pop(0)
        p2card = p2deck.pop(0)
        if len(p1deck) >= p1card and len(p2deck) >= p2card:
            winner, _ = play_rcombat_game(p1deck[:p1card], p2deck[:p2card])
            if winner == 1:
                p1deck.append(p1card)
                p1deck.append(p2card)
            else:
                p2deck.append(p2card)
                p2deck.append(p1card)
        else:
            if p1card > p2card:
                p1deck.append(p1card)
                p1deck.append(p2card)
            else:
                p2deck.append(p2card)
                p2deck.append(p1card)

    if len(p2deck) == 0:
        return 1, p1deck
    return 2, p2deck

@timed
def part_two(p1deck, p2deck):
    # Part 2 takes ~18 seconds to run, good enough
    winner, winning_deck = play_rcombat_game(p1deck, p2deck)

    score = 0
    for i, card in enumerate(winning_deck[::-1]):
        score += card * (i + 1)

    return score


print(part_one(p1deck.copy(), p2deck.copy()))
print(part_two(p1deck.copy(), p2deck.copy()))
