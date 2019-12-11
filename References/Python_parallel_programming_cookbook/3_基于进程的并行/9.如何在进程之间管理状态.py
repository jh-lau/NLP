"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

from multiprocessing import Process, Manager


def worker(dictionary, key, item):
    dictionary[key] = item
    print(f"key = {key}; value =  {item}")


if __name__ == '__main__':
    mgr = Manager()
    dictionary = mgr.dict()
    jobs = [Process(target=worker, args=(dictionary, i, i * 2))
            for i in range(10)]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print('Results:', dictionary)
