import multiprocessing


def foo(i):
    print(f'called function in process {i}')
    return


if __name__ == '__main__':
    process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        process_jobs.append(p)
        p.start()
        p.join()
