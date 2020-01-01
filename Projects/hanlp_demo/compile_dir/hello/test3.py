"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

import click


@click.command()
@click.option('--name', '-n', help='name, optional', default='liujianhan')
@click.option('--year', help='year optional', type=int)
@click.option('--body', help='body')
def test_for_sys(year, name, body):
    print(f"The year is {year}")
    print(f"The name is {name}")
    print(f"The body is {body}")


if __name__ == '__main__':
    try:
        test_for_sys()
    except Exception as e:
        print(f'Error with {e}')
