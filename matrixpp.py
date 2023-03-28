# matrixpp

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    r = int(input("Enter row length: "))
    print("MATRIX 1: ")
    array = []
    for i in range(r):
        row = []
        for j in range(r):
            row.append(int(input("Enter data [{0} , {1}]".format(i+1, j+1))))
        array.append(row)
    req = comm.isend(array, dest=1, tag=11)
    req.wait()

    print("\n\nMATRIX 2: ")
    array = []
    for i in range(r):
        row = []
        for j in range(r):
            row.append(int(input("Enter data [{0} , {1}]".format(i+1, j+1))))
        array.append(row)
    req = comm.isend(array, dest=1, tag=11)
    req.wait()

elif rank == 1:
    req = comm.irecv(source=0, tag=11)
    data1 = req.wait()
    print(data1)
    req = comm.irecv(source=0, tag=11)
    data2 = req.wait()
    print(data2)
    result = [[None for x in range(len(data1))] for x in range(len(data1))]
    for i in range(len(data1)):
        for j in range(len(data1)):
            for k in range(len(data1)):
                result[i][j] = data1[i][k]*data2[k][j]
    print(result)