#mpiexec -n 5 python main.py

import numpy as np
from mpi4py import MPI
import time
import math

def picount(dots):
    in_circle = np.count_nonzero(((dots.T[0])*(dots.T[0]) + (dots.T[1])*(dots.T[0])) <= 1)
    pi = 4.0*in_circle/len(dots)
    return pi

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = None
if rank == 0:
    amount_of_dots=10000000
    dots = np.random.rand(amount_of_dots,2)
    data = [dots[0: (i + 1) * math.ceil(amount_of_dots/size)] for i in range(0, size)]

a = comm.scatter(data, root=0)

time_start = time.time()
pi = picount(a)
time = time.time()
info = comm.gather({"pi": pi, "time": time}, root=0)

if rank == 0:
    for i in info:
        print("pi:", i["pi"], "time:", i["time"])
