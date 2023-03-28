#pi broad

from mpi4py import MPI
import numpy as np
import math
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
s=0
n=1000000
if rank == 0:
    for i in range(int (n*0.25)):
        s += 1 / (i*4.0 + 1) - 1 / (i * 4.0 + 3)
elif rank==1:
    for i in range(int (n*0.25)):
        s += 1 / (i*4.0 + 1) - 1 / (i * 4.0 + 3)

elif rank==2:
    for i in range(int (n*0.25)):
        s += 1 / (i*4.0 + 1) - 1 / (i * 4.0 + 3)
elif rank==3:
    for i in range(int (n*0.25)):
        s += 1 / (i*4.0 + 1) - 1 / (i * 4.0 + 3)
# print(rank,PI)
PI = comm.reduce(s,op=MPI.SUM,root=0)
print("Before Broadcast : ",rank,PI)
print("After Broadcast",rank,PI)