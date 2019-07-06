"""
  User: Liujianhan
  Time: 17:14
 """
from functools import update_wrapper

__author__ = 'liujianhan'


def decorator(d):
    """Make function d a decorator: d wraps a function fn."""

    def _d(fn):
        return update_wrapper(d(fn), fn)

    update_wrapper(_d, d)
    return _d


@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    then when called again with same args, we can just look it up."""
    cache = {}

    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)

    return _f


@decorator
def count_calls(f):
    """Decorator that makes the function count calls to it, in call_counts[f]"""

    def _f(*args):
        call_counts[_f] += 1
        return f(*args)

    call_counts[_f] = 0
    return _f


call_counts = {}


@decorator
# @memo
def fib(n):
    return 1 if n <= 1 else fib(n - 1) + fib(n - 2)


@decorator
def trace(f):
    indent = '  '

    def _f(*args):
        signature = f"{f.__name__}({', '.join(map(repr, args))})"
        print(f"{trace.level * indent}--> {signature}")
        trace.level += 1
        try:
            result = f(*args)
            print(f"{(trace.level - 1) * indent}<-- {signature} === {result}")
        finally:
            trace.level -= 1
        return result

    trace.level = 0
    return _f


if __name__ == '__main__':
    print(fib(10))
