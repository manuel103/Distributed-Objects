from mpi4py import MPI


comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
p = comm.Get_size()

if my_rank == 1:
    comm.send(2/2, dest=0)
elif my_rank == 2:
    comm.send(4 + 5, dest=0)
elif my_rank == 3:
    comm.send(2 * (6 + 6 + 4 + 4), dest=0)
else:
    from_1 = int(comm.recv(source=1))
    print("Process 1 = ", from_1)

    from_2 = int(comm.recv(source=2))
    print("Process 2 = ", from_2)

    from_3 = int(comm.recv(source=3))
    print("Process 3 = ", from_3)

    area = from_1 * (from_2 + from_3)
    print("Area is = ", area)
