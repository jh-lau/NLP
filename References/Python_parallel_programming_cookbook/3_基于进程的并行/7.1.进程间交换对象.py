"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

import random
import time
from multiprocessing import Process, Queue


class Producer(Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print(f'Process Producer: item {item} appended to queue {self.name}')
            time.sleep(1)
            print(f'The size of queue is {self.queue.qsize()}')


class Consumer(Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print('The queue is empty')
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print(f'Processs Consumer: item {item} popped from by {self.name}')
                time.sleep(1)


if __name__ == '__main__':
    queue = Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)
    process_producer.start()
    time.sleep(1)
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
