# kendall-rank-correlation-coefficient with Parallelization

This repository contains a project for the course "Parallel Algorithms for Data Synthesis and Analysis". The project presents sequential and parallel implementations of the algorithm for finding the Kendall rank correlation coefficient.


The goal of the project is to clearly demonstrate the reduction of the algorithm's running time by applying the concept of parallel computing.

---

## Algorithm Overview:

The code computes the Kendall rank correlation coefficient (tau) using both sequential and parallel approaches. The sequential method iterates through all pairs of elements to count concordant and discordant pairs. The parallel method divides the workload among multiple processes using MPI, where each process calculates its portion of the data and then reduces the results to get the final tau.

---

## Tools Used:

• numpy: For generating random vectors.

• mpi4py: For parallel processing using the MPI standard.

• scipy: For calculating Kendall's tau using a built-in function.

---

## Usage Instructions:

1. Install the required libraries:
```bash
    pip install numpy mpi4py scipy
```
2. Run the script with the required arguments:
```bash
    mpiexec -n <num_workers> python script.py <length> <min_value> <max_value> <num_workers>
```

---

## Parallelization Principle:

The input vectors are divided into chunks based on the number of workers. Each worker processes its chunk independently and computes local counts of concordant and discordant pairs.The results are collected from each stream using a reduce operator and summed by a computer to give the final value of Kendall's tau.

---

## Visualisation program Overview:

The graph_efficiency program runs the previously defined script with varying numbers of workers (from 1 to 10) and captures the execution time for the parallel computation. It then plots this time against the number of worker processes using Matplotlib, producing a handy png file that can be used to analyze the efficiency of dividing the work by calculating the coefficient.

---

## Usage Instructions:

1. Make sure you have matplotlib installed:
```bash
    pip install matplotlib
```
2. Run the graphing script:
```bash
    python graph_script.py>
```

---

## Results
As a result of running the program on our machine for 8 workers, an array of 2000 elements with values ​​from 2 to 50, we received the following time values:
- Non-parallel execution time: **~1.39 seconds**  
- Parallel execution time: **~0.23 seconds (6x speedup)**
- ScyPy execution time **~0.0 seconds** ☠☠☠

Also, you can look at the efficiency of dividing the workflow into workers to speed up the algorithm:
![Speed up results](https://github.com/BibAss/kendall-rank-correlation-coefficient/blob/main/img/img.png?raw=true)
