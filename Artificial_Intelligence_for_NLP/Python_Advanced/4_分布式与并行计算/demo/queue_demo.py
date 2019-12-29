from multiprocessing import Process, Pool, Queue
import multiprocessing


def f(name):
    print(f"thread {multiprocessing.current_process().name}")
    print(f"Hello {name}")

def f_1(x):
    return x * x

def f_2(q):
    q.put([1, 2, "xx", "yy"])

if __name__ == '__main__':
    print(f"thread {multiprocessing.current_process().name}")
    cpus = multiprocessing.cpu_count()
    print(f"Cpus: {cpus}")
    # p = Process(target=f, args=("Rambo", ))
    # p.start()
    # p.join()
    # with Pool(cpus) as p:
    #     print(p.map(f_1, list(range(100))))

    q = Queue()
    p = Process(target=f_2, args=(q, ))
    p.start()
    print(q.get())
    p.join()