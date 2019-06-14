"""
  User: Liujianhan
  Time: 14:21
  clubs (♣), diamonds (♦), hearts (♥), spades (♠)
  straight flush 8 > four of a kind 7 > full house 6 > flush 5
  > straight 4 > three of a kind 3 > two pair 2 > one pair 1 > high card 0
 """
__author__ = 'liujianhan'


def poker(hands):
    """
    :param hands:
    :return: return the best hand: poker([hand,...]) => hand
    """
    return max(hands, key=hand_rank)


def hand_rank(hand):
    """
    :param hand:
    :return: return a value indicating the ranking of hand.
    """
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):  # straight flush
        return 8, max(ranks)
    elif kind(4, ranks):  # 4 of a kind
        return 7, kind(4, ranks), kind(1, ranks)
    elif kind(3, ranks) and kind(2, ranks):  # full house
        return 6, kind(3, ranks), kind(2, ranks)
    elif flush(hand):  # flush
        return 5, ranks
    elif straight(ranks):  # straight
        return 4, ranks[0]
    elif kind(3, ranks):  # 3 of a kind
        return 3, kind(2, ranks), ranks
    elif two_pair(ranks):  # two pair
        return 2, two_pair(ranks), ranks
    elif kind(2, ranks):  # 2 of a kind
        return 1, kind(2, ranks), ranks
    else:  # high card
        return 0, ranks


def card_ranks(hand):
    """
    :param hand:
    :return: return a list of the ranks, sorted with higher first
    """
    ranks = ['--23456789TJQKA'.index(r) for r, _ in hand]
    ranks.sort(reverse=True)
    return ranks


def straight(ranks):
    """
    :param ranks:
    :return: return true if the ordered ranks form a 5-card straight
    """
    # new = [r for r in range(ranks[0], len(ranks) + 1, -1)]
    # return True if ranks == new else False
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    """
    :param hand:
    :return: return true if all the cards have same suit
    """
    suits = [s for _, s in hand]
    return len(set(suits)) == 1


def kind(n, ranks):
    """
    :param n:
    :param ranks:
    :return: return the first rank that this hand has exactly n of.
    """
    for i in ranks:
        if ranks.count(i) == n:
            return i
    return None


def two_pair(ranks):
    """
    :param ranks:
    :return: return the two ranks as tuple:(highest, lowest) if there are two pair or None
    """
    pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if pair and low_pair != pair:
        return pair, low_pair
    else:
        return None


def test():
    # straight flush
    sf = '6C 7C 8C 9C TC'.split()
    # four of a kind
    fk = '9D 9H 9S 9C 7D'.split()
    # full house
    fh = 'TD TC TH 7C 7D'.split()
    # two pair
    tp = '5S 5D 9H 9C 6S'.split()
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) is None
    assert kind(2, fkranks) is None
    assert kind(1, fkranks) == 7
    assert two_pair(fkranks) is None
    assert two_pair(tpranks) == (9, 5)
    assert straight([9, 8, 7, 6, 5]) is True
    assert straight([9, 8, 8, 6, 5]) is False
    assert flush(sf) is True
    assert flush(fk) is False
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99 * [fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return 'test pass'


if __name__ == '__main__':
    print(test())
