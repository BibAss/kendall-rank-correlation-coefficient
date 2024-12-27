import numpy as np
import time
import sys
from mpi4py import MPI
from scipy.stats import kendalltau

def kendall_tau_sequential(x, y):
    n = len(x)
    concordant = discordant = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (x[i] - x[j]) * (y[i] - y[j]) > 0:
                concordant += 1
            elif (x[i] - x[j]) * (y[i] - y[j]) < 0:
                discordant += 1
    return (concordant - discordant) / (0.5 * n * (n - 1))

def kendall_tau_parallel(x, y):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    n = len(x)
    local_n = n // size
    local_x = x[rank * local_n:(rank + 1) * local_n]
    local_y = y[rank * local_n:(rank + 1) * local_n]

    local_concordant = local_discordant = 0
    for i in range(local_n):
        for j in range(i + 1, local_n):
            if (local_x[i] - local_x[j]) * (local_y[i] - local_y[j]) > 0:
                local_concordant += 1
            elif (local_x[i] - local_x[j]) * (local_y[i] - local_y[j]) < 0:
                local_discordant += 1

    global_concordant = comm.reduce(local_concordant, op=MPI.SUM, root=0)
    global_discordant = comm.reduce(local_discordant, op=MPI.SUM, root=0)

    if rank == 0:
        return (global_concordant - global_discordant) / (0.5 * n * (n - 1))
    return None

if len(sys.argv) != 4:
    print("Usage:mpiexec -n <num_workers> python script.py <length> <min_value> <max_value>")
    exit(0)

length = int(sys.argv[1])
min_value = int(sys.argv[2])
max_value = int(sys.argv[3])

np.random.seed(42)
x = np.random.randint(min_value, max_value + 1, size=length)
y = np.random.randint(min_value, max_value + 1, size=length)

	# Sequential calculation
start_time = time.time()
tau_sequential = kendall_tau_sequential(x, y)
sequential_time = time.time() - start_time

	# Parallel calculation
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
    
start_time = time.time()
tau_parallel = kendall_tau_parallel(x, y)
parallel_time = time.time() - start_time

	# Scipy calculation
start_time = time.time()
tau_scipy, _ = kendalltau(x, y)
scipy_time = time.time() - start_time

if rank == 0:
    print(f"Sequential Time: {sequential_time:.6f}, Tau: {tau_sequential:.6f}")
    print(f"Parallel Time: {parallel_time:.6f}, Tau: {tau_parallel:.6f}")
    print(f"SciPy Time: {scipy_time:.6f}, Tau: {tau_scipy:.6f}")
