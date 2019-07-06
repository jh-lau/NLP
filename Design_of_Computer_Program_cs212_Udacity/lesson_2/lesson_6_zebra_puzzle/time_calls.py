"""
  User: Liujianhan
  Time: 18:01
 """
import time

__author__ = 'liujianhan'


def timed_call(fn, *args):
    start = time.perf_counter_ns()
    result = fn(*args)
    end = time.perf_counter_ns()
    tot = (end - start) / 10 ** 9
    return tot, result


def average(numbers):
    return sum(numbers) / float(len(numbers))


def timed_calls(n, fn, *args):
    """ Call fn(*args) repeatedly: n times if n is an int, or up to n seconds if n is a
    float; return the min, avg, and max time."""
    if isinstance(n, int):
        times = [timed_call(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append((timed_call(fn, *args)[0]))
    return min(times), average(times), max(times)


def ints(start=0, end=None):
    """A generator function never stops when end equal to none."""
    i = start
    while end is None or i <= end:
        yield i
        i += 1


def all_ints(start=1, end=None):
    """Generate integers in the order 0, 1, -1, 2, -2, 3, -3, ...."""
    yield 0
    for i in ints(start, end):
        yield +i
        yield -i


def instrument_fn(fn, *args):
    c.starts, c.items = 0, 0
    result = fn(*args)
    # todo
    print("%s got %s with %5d iters over %7d items" % (fn.__name__, result, c.starts, c.items))


def c(sequence):
    """Generate items in sequence; keeping counts as we go. c.start is the number of
    sequences started; c.items is number of items generated."""
    # todo
    c.start += 1
    for item in sequence:
        c.items += 1
        yield item


if __name__ == '__main__':
    print(list(ints(1, 10)))
    print(list(all_ints(3, 10)))
