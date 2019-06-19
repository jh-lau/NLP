"""
  User: Liujianhan
  Time: 21:50
 """
from functools import update_wrapper

__author__ = 'liujianhan'


def lit(s):
    return lambda ns: {s} if len(s) in ns else null


def alt(x, y):
    return lambda ns: x(ns) | y(ns)


def star(x):
    return lambda ns: opt(plus(x))(ns)


def plus(x):
    return lambda ns: genseq(x, star(x), ns, start_x=1)  # Tricky


def oneof(chars):
    return lambda ns: {chars} if 1 in ns else null


def seq(x, y):
    return lambda ns: genseq(x, y, ns)


def opt(x):
    return alt(epsilon, x)


dot = oneof('?')  # You could expand the alphabet to more chars.
epsilon = lit('')  # The pattern that matches the empty string.

null = frozenset([])


def genseq(x, y, ns, start_x=0):
    """Tricky part: x+ is defined as: x+ = x x*
    To stop the recursion,the first x must generate at least 1 char,
    and then the recursive x* has that many fewer characters. We use
    start_x=1 to say that x must match at least 1 character"""
    if not ns:
        return null
    # todo
    x_matches = x({range(start_x, max(ns) + 1)})
    ns_x = {len(m) for m in x_matches}
    ns_y = {n - m for n in ns for m in ns_x if n - m >= 0}
    y_matches = y(ns_y)
    return {m1 + m2 for m1 in x_matches
            for m2 in y_matches if len(m1 + m2) in ns}


def decorator(d):
    """Make function d a decorator: d wraps a function fn."""

    def _d(fn):
        return update_wrapper(d(fn), fn)

    update_wrapper(_d, d)
    return _d


@decorator
def n_ary(f):
    """Given binary function f(x,y), return an n_ary function such
    that f(x, y, z) = f(x, f(y, z)), etc. Also allow f(x) = x."""

    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary(*args))

    return n_ary_f


def test_gen():
    def n(hi):
        return {range(hi + 1)}

    a, b, c = map(lit, 'abc')
    assert star(oneof('ab'))(n(2)) == {'', 'a', 'aa', 'ab', 'ba', 'bb', 'b'}
    assert (seq(star(a), seq(star(b), star(c)))({4})) == {
        'aaaa', 'aaab', 'aaac', 'aabb', 'aabc', 'aacc', 'abbb', 'abbc',
        'abcc', 'accc', 'bbbb', 'bbbc', 'bbcc', 'bccc', 'cccc'
    }
    assert (seq(plus(a), seq(plus(b), plus(c)))({5})) == {'aaabc', 'aabbc',
                                                          'aabcc', 'abbbc', 'abbcc', 'abccc'}
    assert (seq(oneof('bcfhrsm'), lit('at'))(n(3))) == {'bat', 'cat', 'fat', 'hat',
                                                        'mat', 'rat', 'sat'}
    assert (seq(star(alt(a, b)), opt(c))({3})) == {'aaa', 'aab', 'aac', 'aba', 'abb', 'abc',
                                                   'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc'}
    assert lit('hello')({5}) == {'hello'}
    assert lit('hello')({4}) == {}
    assert lit('hello')({6}) == {}
    return 'test_gen passes'


if __name__ == '__main__':
    print(test_gen())
