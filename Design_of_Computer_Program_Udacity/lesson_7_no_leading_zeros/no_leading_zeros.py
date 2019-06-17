"""
  User: Liujianhan
  Time: 14:01
 """
__author__ = 'liujianhan'
import re
import itertools


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('%s*%s' % (10 ** i, d))
                 for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word


def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as parms of function. The first digit of a multi-digit
    number can't be 0. So if YOU is a word in the formula, and the function
    is called with Y equal to 0, the function should return False.
    e.g:'YOU == ME**2' returns (lambda Y, M, E, U, O: Y!=0 and M!=0 and (U+10*O+100*Y) == (E+10*M)**2), 'YMEUO'"""

    # modify the code in this function.

    letters = ''.join(set(re.findall('[A-Z]', formula)))
    first_letters = set(re.findall(r'\b([A-Z])[A-Z]', formula))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    if first_letters:
        tests = ' and '.join(ch+'!=0' for ch in first_letters)
        body = f"{tests} and ({body})"
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
            pass


def test():
    assert faster_solve('A + B == BA') is None  # should NOT return '1 + 0 == 01'
    assert faster_solve('YOU == ME**2') == ('289 == 17**2' or '576 == 24**2' or '841 == 29**2')
    assert faster_solve('X / X == X') == '1 / 1 == 1'
    return 'tests pass'


if __name__ == '__main__':
    test()
