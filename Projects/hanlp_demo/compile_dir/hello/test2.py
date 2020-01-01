"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

import argparse


def test_for_sys(year, name, body):
    print(f"The year is {year}")
    print(f"The name is {name}")
    print(f"The body is {body}")


parser = argparse.ArgumentParser(description='Test for args parser')
parser.add_argument('--name', '-n', help='name, optional')
parser.add_argument('--year', '-y', help='year, optional', default=2020)
parser.add_argument('--body', '-b', help='body, required', required=True)
args = parser.parse_args()

if __name__ == '__main__':
    try:
        test_for_sys(args.year, args.name, args.body)
        print(f"args: {args}")
    except:
        print('wrong')
        print(f"args: {args}")
