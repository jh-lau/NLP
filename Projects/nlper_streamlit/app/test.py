"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

import multiprocessing


def f(x):
    return x * 2


with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
    print(p.map(f, list(range(10))))
