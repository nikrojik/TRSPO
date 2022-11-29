import random
import threading
import time
class Data:
    def __init__(self):
        self.data = 0
    def set(self, value):
        self.data = value
    def get(self):
        return self.data

def func(status, first, second):
    iter = random.randint(10_000, 20_000)

    for i in range(iter):
        status.acquire()
        a = random.randint(0, 9) + first.get()
        first.set(a)
        a = random.randint(0, 9) + second.get()
        second.set(a)
        status.release()

time_start = time.time()
first = Data()
second = Data()

threads_amount = random.randint(10, 20)
status = threading.Lock()

for i in range(threads_amount):
    thr = threading.Thread(target=func, args=(status, first, second)).start()

print("WORK FINISHED")
print("time:", time.time() - time_start)
