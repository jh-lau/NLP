"""
  User: Liujianhan
 """
__author__ = 'liujianhan'

from multiprocessing import Process, Pipe


def create_time(pipe):
    output_pipe, _ = pipe
    for item in range(10):
        output_pipe.send(item)
    output_pipe.close()


def multiply_items(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            item = input_pipe.recv()
            output_pipe.send(item * item)
    except EOFError:
        output_pipe.close()


if __name__ == '__main__':
    pipe_1 = Pipe(True)
    process_pipe1 = Process(target=create_time, args=(pipe_1,))
    process_pipe1.start()

    pipe_2 = Pipe(True)
    process_pipe2 = Process(target=multiply_items, args=(pipe_1, pipe_2))
    process_pipe2.start()
    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            print(pipe_2[1].recv())
    except EOFError:
        print('End')
