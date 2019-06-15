"""
  User: Liujianhan
  Time: 13:55
 """
from collections import defaultdict

__author__ = 'liujianhan'
import random


def deal(num_hands, n=5, deck=[r + s for r in '23456789TJQKA' for s in 'SHDC']):
    """
    :param num_hands:
    :param n:
    :param deck:
    :return: shuffle the deck and deal out numbers n-card hands.
    """
    random.shuffle(deck)
    return [deck[n * i:n * (i + 1)] for i in range(num_hands)]


def bad_shuffle(deck):
    # O(n2) and not correct
    n = len(deck)
    swapped = [False] * n
    while not all(swapped):
        i, j = random.randrange(n), random.randrange(n)
        swapped[i] = swapped[j] = True
        swap(deck, i, j)


def good_shuffle(deck):
    # O(n) and correct
    n = len(deck)
    for i in range(n - 1):
        swap(deck, i, random.randrange(i, n))


def shuffle_2(deck):
    # O(n2) but correct
    n = len(deck)
    swapped = [False] * n
    while not all(swapped):
        i, j = random.randrange(n), random.randrange(n)
        swapped[i] = True
        swap(deck, i, j)


def shuffle_3(deck):
    # O(n) but not correct
    n = len(deck)
    for i in range(n):
        swap(deck, i, random.randrange(n))


def swap(deck, i, j):
    # print(f"swap {i} {j}")
    deck[i], deck[j] = deck[j], deck[i]


def test_shuffler(shuffler, deck='abcd', n=10000):
    counts = defaultdict(int)
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] += 1
    e = n * 1. / factorial(len(deck))
    ok = all((0.9 <= counts[item] / e <= 1.1) for item in counts)
    name = shuffler.__name__
    print("%s(%s) %s" % (name, deck, ('ok' if ok else '***BAD***')))
    for item, count in sorted(counts.items()):
        print("%s: %4.1f %%" % (item, count * 100. / n))
    print()


def test_shufflers(shufflers=[good_shuffle], decks=['abc', 'abcf']):
    for deck in decks:
        print()
        for f in shufflers:
            test_shuffler(f, deck)


def factorial(n):
    return 1 if (1 >= n) else n*factorial(n - 1)


if __name__ == '__main__':
    test_shufflers()
