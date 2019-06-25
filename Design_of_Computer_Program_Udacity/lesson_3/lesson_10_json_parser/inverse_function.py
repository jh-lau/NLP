"""
  User: Liujianhan
  Time: 23:01
 """
__author__ = 'liujianhan'


def slow_inverse(f, delta=1 / 128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negative numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""

    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        return x if (f(x) - y < y - f(x - delta)) else x - delta

    return f_1


def inverse(f, delta=1 / 1024.):
    def f_1(y):
        low, high = find_bounds(f, y)
        return binary_search(f, y, low, high, delta)

    return f_1


def find_bounds(f, y):
    """Find values low, high such f(low) <= y <= f(high).
    Keep doubling x until f(x) >= y; that's high;
    and low will be either the previous x or 0"""
    x = 1
    while f(x) < y:
        x *= 2
    low = 0 if 1 == x else x / 2
    return low, x


def binary_search(f, y, low, high, delta):
    """Give f(low) <= y <= f(high), return x such that f(x) is within delta of y.
    Continually split the region in half"""
    while low <= high:
        x = low + (high - low) / 2.
        if f(x) < y:
            low = x + delta
        elif f(x) > y:
            high = x - delta
        else:
            return x
    return high if (f(high) - y < y - f(low)) else low


@inverse
def square(x):
    return x * x


@inverse
def power_10(x):
    return 10 ** x


@inverse
def power_3(x):
    return x ** 3


def test():
    import math
    nums = [2, 4, 6, 8, 10, 99, 100, 101, 1000, 10000, 20000, 40000, 100000000]
    for n in nums:
        test1(n, 'sqrt', square(n), math.sqrt(n))
        test1(n, 'log ', power_10(n), math.log10(n))
        test1(n, '3-rt', power_3(n), n ** (1. / 3.))


def test1(n, name, value, expected):
    diff = abs(value - expected)
    print(f"{n:6g}: {name} ={value:13.7f} ({expected:13.7f} expected); {diff: .4f} diff; "
          f"{'ok' if diff < .002 else '*** BAD ***'}")


if __name__ == '__main__':
    test()
