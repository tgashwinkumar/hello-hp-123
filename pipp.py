# pipp

from mpi4py import MPI
import numpy as np
import random


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


# Number of iterations for each process
num_iter = 1000000 // size


# Initialize local count of points inside the circle
local_count = 0


# Generate random points and count those inside the circle
for i in range(num_iter):
   x = random.uniform(-1, 1)
   y = random.uniform(-1, 1)
   if x*2 + y*2 <= 1:
       local_count += 1


# Send local count to the master process
if rank == 0:
   count = local_count
   for i in range(1, size):
       count += comm.recv(source=i)
else:
   comm.send(local_count, dest=0)


# Calculate and print the value of pi
if rank == 0:
   pi = 4 * count / (size * num_iter)
   print("pi =", pi)
