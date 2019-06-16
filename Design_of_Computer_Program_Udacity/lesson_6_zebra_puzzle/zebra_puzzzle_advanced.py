"""
  User: Liujianhan
  Time: 17:25
 """
from function_process_time import RuntimeTest

__author__ = 'liujianhan'
import itertools
from lesson_6_zebra_puzzle.time_calls import timed_calls, timed_call


def im_right(h1, h2):
    """House h1 is immediately right of h2 if h1-h2 == 1"""
    return 1 == h1 - h2


def next_to(h1, h2):
    """Two houses are next to each other if they differ by 1"""
    return 1 == abs(h1 - h2)


@RuntimeTest(10)
def zebra_puzzle():
    """Return a tuple (WATER, ZEBRA) indicating their house numbers
    More efficient after change the clause order."""
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                if im_right(green, ivory)
                for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings
                if Englishman is red
                if Norwegian is first
                if next_to(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in orderings
                if milk is middle
                if coffee is green
                if Ukrainian is tea
                for (OldGold, Kools, ChesterFields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow
                if oj is LuckyStrike
                if Parliaments is Japanese
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog
                if OldGold is snails
                if next_to(ChesterFields, fox)
                if next_to(Kools, horse)
                )


if __name__ == '__main__':
    print(zebra_puzzle())
    print(timed_call(zebra_puzzle))
    print(timed_calls(10, zebra_puzzle))

