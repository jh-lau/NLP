from multiprocessing import Process, Pool
import multiprocessing


def f(name):
    print(f"thread {multiprocessing.current_process().name}")
    print(f"Hello {name}")

def f_1(x):
    return x * x

if __name__ == '__main__':
    print(f"thread {multiprocessing.current_process().name}")
    cpus = multiprocessing.cpu_count()
    print(f"Cpus: {cpus}")
    # p = Process(target=f, args=("Rambo", ))
    # p.start()
    # p.join()
    with Pool(cpus) as p:
        print(p.map(f_1, list(range(100))))




