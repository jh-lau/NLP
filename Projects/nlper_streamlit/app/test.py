"""
  User: Liujianhan
 """
from functools import wraps

__author__ = 'liujianhan'
import time
from threading import Lock

def run_time_calc(func):
    @wraps(func)
    def wrapper(*args):
        start_time = time.time()
        print(args)
        print(*args)
        func(*args)
        end_time = time.time()
        cost = end_time - start_time
        print(f"{func.__name__} cost {cost} seconds.")

    return wrapper


@run_time_calc
def add(n):
    i = 0
    for _ in range(n):
        i += _
    return i


dict()
super()


class C(object):
    @property
    def x(self):
        "I am the 'x' property."
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


if __name__ == '__main__':
    # print(add(100000))
    pass


