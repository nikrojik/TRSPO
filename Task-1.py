import threading

def sum(a, b):
    print(a + b)

thr1 = threading.Thread(target=sum, args = (1, 2))
thr2 = threading.Thread(target=sum, args = (3, 4))
thr1.start()
thr2.start()
