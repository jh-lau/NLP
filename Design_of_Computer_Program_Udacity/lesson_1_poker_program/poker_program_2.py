"""
  User: Liujianhan
  Time: 14:21
  clubs (♣), diamonds (♦), hearts (♥), spades (♠)
  straight flush 8 > four of a kind 7 > full house 6 > flush 5
  > straight 4 > three of a kind 3 > two pair 2 > one pair 1 > high card 0
 """
import random

__author__ = 'liujianhan'


def poker(hands):
    """
    :param hands:
    :return: return the best hand: poker([hand,...]) => [hand,...] to solve tie like
    '6C 7C 8C 9C TC' and '6D 7D 8D 9D TD', should return both instead one of them
    """
    return all_max(hands, key=hand_rank_new)


def hand_rank_new(hand):
    groups = group(['--23456789TJQKA'.index(r) for r, _ in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([s for _, s in hand])) == 1
    return (
               9 if (5,) == counts else
               8 if straight and flush else
               7 if (4, 1) == counts else
               6 if (3, 2) == counts else
               5 if flush else
               4 if straight else
               3 if (3, 1, 1) == counts else
               2 if (2, 2, 1) == counts else
               1 if (2, 1, 1, 1) == counts else
               0
           ), ranks


def all_max(iterable, key=None):
    """
    :param iterable:
    :param key:
    :return: return a list of all items equal to the max of the iterable
    """
    result, max_val = [], None
    key = key or (lambda x: x)
    for x in iterable:
        x_val = key(x)
        if not result or x_val > max_val:
            result, max_val = [x], x_val
        elif x_val == max_val:
            result.append(x)
    return result


def deal(num_hands, n=5, deck=[r + s for r in '23456789TJQKA' for s in 'SHDC']):
    """
    :param num_hands:
    :param n:
    :param deck:
    :return: shuffle the deck and deal out numbers n-card hands.
    """
    random.shuffle(deck)
    return [deck[n * i:n * (i + 1)] for i in range(num_hands)]


def hand_percentages(n=700 * 1000):
    """
    :param n:
    :return: sample n random hands and print a table of percentages for each type of hand
    """
    hand_names = ['Straight Flush: 0.0015 %',
                  'Four of a kind: 0.024 %',
                  'Full House: 0.140 %',
                  'Flush: 0.196 %',
                  'Straight: 0.39 %',
                  'Three of a kind: 2.11 %',
                  'Two pair: 4.75 %',
                  'Pair: 42.25 %',
                  'High Card: 50.11 %']
    counts = [0] * 9
    for i in range(n // 10):
        for hand in deal(10):
            ranking = hand_rank_new(hand)[0]
            counts[ranking] += 1
    counts.reverse()
    for i in (range(9)):
        print("%25s vs %6.4f %%" % (hand_names[i], 100. * counts[i] / n))


def group(items):
    """
    :param items:
    :return: return a list of [(count, x)...], highest count first, then highest x first.
    """
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)


def unzip(pairs):
    return zip(*pairs)


def test():
    # five of a kind with wild cards or multiple decks
    fk_5 = '5T 5C 5H 5D 5H'.split()
    # straight flush
    sf = '6C 7C 8C 9C TC'.split()
    sf_2 = '6D 7D 8D 9D TD'.split()
    # four of a kind
    fk = '9D 9H 9S 9C 7D'.split()
    # full house
    fh = 'TD TC TH 7C 7D'.split()
    # two pair
    tp = '5S 5D 9H 9C 6S'.split()
    # A-5 straight
    s1 = 'AS 2S 3S 4S 5C'.split()
    # 2-6 straight
    s2 = '2C 3C 4C 5S 6S'.split()
    # A high
    ah = 'AS 2S 3S 4S 6C'.split()
    # 7 high
    sh = '2S 3S 4S 6C 7D'.split()
    print(poker([fk_5]))
    assert poker([s1, s2, ah, sh]) == [s2]
    assert poker([s1, ah, sh]) == [s1]
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([sf]) == [sf]
    assert poker([sf] + 99 * [fh]) == [sf]
    assert poker([sf, sf_2]) == [sf, sf_2]
    return 'test pass'


if __name__ == '__main__':
    test()
    # print(deal(3))
    # print(deal(4, 7))
    # hand_percentages(7000)
