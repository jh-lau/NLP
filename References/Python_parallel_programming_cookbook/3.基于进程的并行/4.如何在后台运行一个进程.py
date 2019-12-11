"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

import time
from multiprocessing import Process, current_process


def foo():
    name = current_process().name
    print(f'Starting {name}')
    time.sleep(2)
    print(f'Exiting {name}')


if __name__ == '__main__':
    back_process = Process(name='back_process', target=foo)
    # 后台进程不允许创建子进程
    back_process.daemon = True
    front_process = Process(name='front_process', target=foo)
    # front_process.daemon = False  # default value
    # front_process.daemon = True
    back_process.start()
    front_process.start()
