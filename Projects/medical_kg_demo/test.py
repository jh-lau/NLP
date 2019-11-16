"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

import os

curdir = os.path.dirname(__file__)
file = os.path.join(curdir, 'dict/deny.txt')
print(file)
with open(file, 'r', encoding='utf-8') as f:
    print(f.read())