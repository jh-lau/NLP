"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

import fileinput

with fileinput.input() as file:
    for line in file:
        print(file.filename(), file.lineno(), line, end='')