"""
  User: Liujianhan
  Time: 15:58

  User Instructions
  Hopper, Kay, Liskov, Perlis, and Ritchie live on
  different floors of a five-floor apartment building.

  Hopper does not live on the top floor.
  Kay does not live on the bottom floor.
  Liskov does not live on either the top or the bottom floor.
  Perlis lives on a higher floor than does Kay.
  Ritchie does not live on a floor adjacent to Liskov's.
  Liskov does not live on a floor adjacent to Kay's.

  where does everyone live?
 """
__author__ = 'liujianhan'
import itertools


def floor_puzzle():
    floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(floors))
    return next([Hopper, Kay, Liskov, Perlis, Ritchie]
                for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
                if Hopper is not top
                if Kay is not bottom
                if Liskov is not top and Liskov is not bottom
                if Perlis > Kay
                if not 1 == abs(Ritchie - Liskov)
                if not 1 == abs(Liskov - Kay)
                )


if __name__ == '__main__':
    print(list(floor_puzzle()))
