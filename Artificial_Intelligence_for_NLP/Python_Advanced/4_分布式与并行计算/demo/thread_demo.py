import threading

def f():
    print("Function called by thread ", threading.current_thread().name)
    for i in range(8):
        print(f"thread {threading.current_thread().name} >>> {i}")

    print(f"thread {threading.current_thread().name} ended")

print(f'thread {threading.current_thread().name} is running...')

t = threading.Thread(target=f, name='LoopThread')
t.start()
t.join()

print(f'thread {threading.current_thread().name} ended.')