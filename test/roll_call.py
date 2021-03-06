from mpi4py import MPI
import time


def run():
	rank = MPI.COMM_WORLD.Get_rank()
	size = MPI.COMM_WORLD.Get_size()
	data = rank
	data = MPI.COMM_WORLD.gather(data, root=0)
	if rank == 0:
		print("Performing Roll Call:")
		for i in range(size):
			if data[i] == i:
				print("Process {0} of {1}: Online".format(i+1,size))
			else:
				print("Process {0} of {1}: Unresponsive".format(i+1, size))
			time.sleep(2)



if __name__ == '__main__':
	run()
