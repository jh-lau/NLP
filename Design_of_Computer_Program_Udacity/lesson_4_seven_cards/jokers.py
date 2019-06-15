"""
  User: Liujianhan
  Time: 19:05
  The
  black joker, '?B', can be used as any spade or club
  and the red joker, '?R', can be used as any heart
  or diamond.
 """
__author__ = 'liujianhan'
from itertools import combinations, product

all_ranks = '23456789TJQKA'
red_cards = [r + s for r in all_ranks for s in 'DH']
black_cards = [r + s for r in all_ranks for s in 'SC']


def best_hand(hand):
    return max(combinations(hand, 5), key=hand_rank)


def best_wild_hand(hand):
    hands = set(best_hand(h) for h in product(*map(replacements, hand)))
    return max(hands, key=hand_rank)


def replacements(card):
    if card == '?B':
        return black_cards
    elif card == '?R':
        return red_cards
    else:
        return [card]


def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return 8, max(ranks)
    elif kind(4, ranks):
        return 7, kind(4, ranks), kind(1, ranks)
    elif kind(3, ranks) and kind(2, ranks):
        return 6, kind(3, ranks), kind(2, ranks)
    elif flush(hand):
        return 5, ranks
    elif straight(ranks):
        return 4, max(ranks)
    elif kind(3, ranks):
        return 3, kind(3, ranks), ranks
    elif two_pair(ranks):
        return 2, two_pair(ranks), ranks
    elif kind(2, ranks):
        return 1, kind(2, ranks), ranks
    else:
        return 0, ranks


def card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def flush(hand):
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


def straight(ranks):
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks):
    pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if pair and low_pair != pair:
        return pair, low_pair
    else:
        return None


def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'


if __name__ == '__main__':
    print(test_best_wild_hand())
