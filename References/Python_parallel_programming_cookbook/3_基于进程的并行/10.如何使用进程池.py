"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

from multiprocessing import Pool, cpu_count


def function_square(data):
    return data * data


if __name__ == '__main__':
    inputs = list(range(10))
    pool = Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)
    pool.close()
    pool.join()
    print('Pool:', pool_outputs)

    # another way of process pool programming
    cpu_counts = cpu_count()
    with Pool(cpu_counts) as p:
        print(p.map(function_square, list(range(10))))

