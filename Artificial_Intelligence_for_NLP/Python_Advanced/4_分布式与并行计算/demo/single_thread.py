from threading import Thread
import time

I = 0

def my_count():
    global I
    while I <= 10000000000:
        I = I + 1

def main():
    start_time = time.time()
    my_count()
    end_time = time.time()
    print(f"Total time : {end_time - start_time}")

if __name__ == '__main__':
    main()
