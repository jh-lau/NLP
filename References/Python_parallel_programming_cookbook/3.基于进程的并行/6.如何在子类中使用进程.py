"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

from multiprocessing import Process


class MyProcess(Process):
    def run(self):
        print(f'called run method in process: {self.name}')
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = MyProcess()
        jobs.append(p)
        p.start()
        p.join()
