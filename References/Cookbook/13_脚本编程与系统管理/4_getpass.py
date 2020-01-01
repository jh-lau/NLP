"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

import getpass


def user_validate(user, passwd):
    print(f"user: {user}")
    print(f"passwd {passwd}")
    if user == 'Liujianhan' and passwd == 'hello world':
        print('Yay!')
    else:
        print('Boo!')


if __name__ == '__main__':
    user = getpass.getuser()
    passwd = getpass.getpass()
    user_validate(user, passwd)
