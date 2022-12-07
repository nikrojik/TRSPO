import threading
from queue import Queue
import time

queue = Queue()

class Data:
    def __init__(self, number):
        self.number = number
        self.previous_num = number
        self.steps = 0

def collatz_func():
    while True:
        if not queue.empty():
            x = queue.get()
            if x.previous_num % 2 != 0:
                x.previous_num = 3 * x.previous_num + 1
            else:
                x.previous_num /= 2
            x.steps += 1
            if x.previous_num == 1:
                continue
            queue.put(x)
        else:
            break

if __name__ == '__main__':
    N = int(input("enter N number:"))
    for i in range(1, N):
        queue.put(item=Data(i))

    threads = int(input("enter amount of threads:"))
    thr = []
    for i in range (1, threads):
        thr.append(threading.Thread(target=collatz_func, args=()))

    time_start = time.time()

    for i in thr:
        i.start()

    for i in thr:
        i.join()

    print("time:", time.time() - time_start)
    print("Finished!")