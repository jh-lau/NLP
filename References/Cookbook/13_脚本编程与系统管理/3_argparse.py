"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

import argparse

parser = argparse.ArgumentParser(description='Search some files')

parser.add_argument(dest='filenames', metavar='filename', nargs='*')
parser.add_argument('-p', '--pat', metavar='pattern',
                    dest='patterns', action='append', help='text pattern to search for')
parser.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')
parser.add_argument('-o', dest='outfile', action='store', help='output file')
parser.add_argument('--speed', dest='speed', action='store', choices=['slow', 'fast'],
                    default='slow', help='search speed')
args = parser.parse_args()
if __name__ == '__main__':
    with open(args.filenames[0], 'r', encoding='utf-8') as f:
        for line in f:
            print(line)
print(args.filenames)
print(args.patterns)
print(args.verbose)
print(args.outfile)
print(args.speed)
