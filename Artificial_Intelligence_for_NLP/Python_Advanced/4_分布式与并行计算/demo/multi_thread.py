from threading import Thread
import time

I = 0

def my_count():
    global I
    while I <= 1000000:
        I = I + 1

def main():
    start_time = time.time()
    threads = []
    for i in range(2):
        t = Thread(target=my_count)
        t.start()
        t.join()
        threads.append(t)

    # for t in threads:
    #     t.join()

    end_time = time.time()
    print(f"Total time : {end_time - start_time}")

if __name__ == '__main__':
    main()