"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print(f'Starting {name}')
    time.sleep(2)
    print(f'Exiting {name}')


if __name__ == '__main__':
    process_with_name = multiprocessing.Process(name='foo_process', target=foo)
    # process_with_name.daemon = True
    process_with_default_name = multiprocessing.Process(target=foo)
    process_with_name.start()
    process_with_default_name.start()
