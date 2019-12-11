"""
  User: Liujianhan
  concurrent.futures:具有线程池和进程池、管理并行编程任务、处理非确定性的执行流程、进程/线程同步等功能。
 """
from multiprocessing import cpu_count

__author__ = 'liujianhan'

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

number_list = list(range(1, 11))


def evaluate_item(x):
    result_item = count(x)
    return result_item


def count(number):
    for i in range(10000000):
        i += 1
    return i * number


if __name__ == '__main__':
    cpus = cpu_count()
    # 顺序执行：5.21s
    start_time = time.time()
    for item in number_list:
        print(evaluate_item(item))
    cost = time.time() - start_time
    print(f'Sequential execution in {cost} seconds.')

    # 线程池执行：GIL影响：5.18s
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=cpus) as executor:
        futures = [executor.submit(evaluate_item, item) for item in number_list]
        for future in as_completed(futures):
            print(future.result())
    print(f"Thread pool execution in {time.time() - start_time} seconds")

    # 进程池执行，不受GIL限制，大大缩短执行时间:2.13s
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=cpus) as executor:
        futures = [executor.submit(evaluate_item, item) for item in number_list]
        for future in as_completed(futures):
            print(future.result())
    print(f"Process pool execution in {time.time() - start_time} seconds")
