import subprocess
import matplotlib.pyplot as plt

def run_kendall(num_workers):
    command = f"mpiexec -n {num_workers} python script.py 1000 0 100"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    for line in result.stdout.splitlines():
        if "Parallel Time" in line:
            time_taken = float(line.split(",")[0].split(":")[1])
            return time_taken
    return None

workers_range = range(1, 11)
times = []

for workers in workers_range:
    time_taken = run_kendall(workers)
    times.append(time_taken)
    print(f"Workers: {workers}, Time: {time_taken:.6f} seconds")

plt.plot(workers_range, times, marker='o')
plt.title('Kendall Tau Calculation Time vs Number of Workers')
plt.xlabel('Number of Workers')
plt.ylabel('Time (seconds)')
plt.grid()
plt.xticks(workers_range)
plt.show()