"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

from datetime import datetime
from multiprocessing import current_process, Barrier, Lock, Process
from time import time


def test_with_barrier(synchronizer, serializer):
    name = current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print(f"process {name} ----> {datetime.fromtimestamp(now)}")


def test_without_barrier():
    name = current_process().name
    now = time()
    print(f"process {name} -----> {datetime.fromtimestamp(now)}")


if __name__ == '__main__':
    synchronizer = Barrier(2)
    serializer = Lock()
    Process(name='p1-test_with_barrier',
            target=test_with_barrier,
            args=(synchronizer, serializer)).start()
    Process(name='p2-test_with_barrier',
            target=test_with_barrier,
            args=(synchronizer, serializer)).start()
    Process(name='p3-test-without_barrier', target=test_without_barrier).start()
    Process(name='p4-test-without_barrier', target=test_without_barrier).start()
