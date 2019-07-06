"""
  User: Liujianhan
  Time: 23:51
  tracking time: python -m cProfile cryptarithmetic.py
 """
import itertools
import time

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


def timed_call(fn, *args):
    start = time.perf_counter_ns()
    result = fn(*args)
    end = time.perf_counter_ns()
    tot = (end - start) / 10 ** 9
    return tot, result


def valid(f):
    """Formula f is valid if it has no numbers with leading zero and evals true."""
    try:
        return not re.findall(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False


def fill_in(formula):
    """Generate all possible fillings-in of letters in formula with digits."""
    letters = ''.join(set(re.findall(r'[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for each in fill_in(formula):
        if valid(each):
            return each
            # return all possible results print or yield
            # yield each
            # print(each)


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""

    # solution 1
    # result = []
    # length = len(word) - 1
    # if word.isupper():
    #     for i, ch in enumerate(word):
    #         num = 10 ** (length - i)
    #         terms = '*'.join([str(num), ch])
    #         result.append(terms)
    #     result.reverse()
    #     return '(' + '+'.join(result) + ')'

    # solution 2
    if word.isupper():
        terms = [f"{10 ** i}*{d}" for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word


def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as parms of function.
    e.g:'YOU == ME**2' returns (lambda Y, M, E, U, O: (U+10*O+100*Y) == (E+10*M)**2), 'YMEUO'"""
    letters = ''.join(set(re.findall(r'[A-Z]', formula)))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = f"lambda {parms}: {body}"
    if verbose:
        print(f)
    return eval(f), letters


def faster_solve(formula):
    """Given a formula lik 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-fill-in string or None.
    This version precompiles the formula; only one eval per formula."""
    f, letters = compile_formula(formula)
    for digits in itertools.permutations(tuple(range(10)), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            return False


def test():
    t0 = time.perf_counter_ns()
    for example in examples:
        print(12 * ' ', example)
        timing, result = timed_call(solve, example)
        # when solve function is generator, use following print clause.
        # print(f"{timing:7.5f} sec: {list(result)}")
        print(f"{timing:7.5f} sec: {result}")
        print('-' * 40)
    print(f"{((time.perf_counter_ns() - t0) / 10 ** 9):6.4f} seconds total.")


def test_fast():
    t0 = time.perf_counter_ns()
    for example in examples:
        print(12 * ' ', example)
        timing, result = timed_call(faster_solve, example)
        # when solve function is generator, use following print clause.
        # print(f"{timing:7.5f} sec: {list(result)}")
        print(f"{timing:7.5f} sec: {result}")
        print('-' * 40)
    print(f"{((time.perf_counter_ns() - t0) / 10 ** 9):6.4f} seconds total.")


if __name__ == '__main__':
    test()  # 0.6 seconds
    # with precompile of eval function, 10 times faster.
    test_fast()  # 0.0664 seconds
