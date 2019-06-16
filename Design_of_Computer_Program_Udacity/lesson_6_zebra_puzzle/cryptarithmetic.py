"""
  User: Liujianhan
  Time: 23:51
 """
import itertools
import time

from lesson_6_zebra_puzzle.time_calls import timed_call

__author__ = 'liujianhan'
import re

tmp = str.maketrans('ABC', '123')
form = 'A+B == C'
s = form.translate(tmp)
eval(s)

examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANETS])""".splitlines()


def valid(f):
    """Formula f is valid if it has no numbers with leading zero and evals true."""
    try:
        return not re.findall(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False


def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for each in fill_in(formula):
        if valid(each):
            # return each
            # return all possible results print or yield
            # yield each
            print(each)


def fill_in(formula):
    """Generate all possible fillings-in of letters in formula with digits."""
    letters = ''.join(set(re.findall(r'[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def test():
    t0 = time.perf_counter_ns()
    for example in examples:
        print(12 * ' ', example)
        timing, result = timed_call(solve, example)
        # when solve function is generator, use following print clause.
        # print('%6.4f sec:  %s ' % (timing, list(result)))
        print(f"{timing:7.5f} sec: {result}")
        print('-' * 40)
    print(f"{((time.perf_counter_ns() - t0) / 10 ** 9):6.4f} seconds total.")


if __name__ == '__main__':
    test()
