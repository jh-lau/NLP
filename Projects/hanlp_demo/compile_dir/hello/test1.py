"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

import sys


def test_for_sys(year, name, body):
    print(f"The year is {year}")
    print(f"The name is {name}")
    print(f"The body is {body}")


if __name__ == '__main__':
    try:
        year, name, body = sys.argv[1:4]
        test_for_sys(year, name, body)
        print(f"sys.argv {sys.argv}")
    except:
        print('wrong')
        print(f"sys.argv {sys.argv}")

