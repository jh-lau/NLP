"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

import os

import click


@click.command()
@click.option('--start', help='target dir', default='.')
@click.option('--name', help='target file', required=True)
@click.option('-h', help='some help messages')
def find_file(start, name):
    for real_path, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, real_path, name)
            print(os.path.normpath(os.path.abspath(full_path)))
            print(os.path.abspath(full_path))


if __name__ == '__main__':
    find_file()
