"""
  User: Liujianhan
  Time: 13:02
 """
__author__ = 'liujianhan'

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    deck = FrenchDeck()
    deck
    print(len(deck))
    print(deck[0])
    print(deck[-1])
    print(deck[:3])
    print(deck[12::13])
    print(Card('Q', 'hearts') in deck)
    print(Card('1Q', 'hearts') in deck)
    for card in sorted(deck, key=spades_high):
        print(card)
