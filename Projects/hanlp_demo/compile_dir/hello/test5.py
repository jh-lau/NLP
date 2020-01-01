"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

import argparse

parser = argparse.ArgumentParser(description='Search some files')

parser.add_argument('--filename', help='filename', required=True)
parser.add_argument('-p', '--pat', help='text pattern to search for')
parser.add_argument('-v', '--verbose', action='store_true', help='verbose mode')
parser.add_argument('-o', help='output file')
parser.add_argument('--speed', choices=['slow', 'fast'],
                    default='slow', help='search speed')
args = parser.parse_args()

print(args.filename)
print(args.pat)
print(args.verbose)
print(args.o)
print(args.speed)
print(dir(args))