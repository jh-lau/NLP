"""
  User: Liujianhan
 """
from functools import wraps

__author__ = 'liujianhan'
import threading
import time


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


if __name__ == '__main__':
    print(add(100000))
