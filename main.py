from classes import Process
import algorithms

def run_simulation():
    user_input = input()

    # Parse input for algorithm, number of processes, and time slice
    if len(user_input.split()) != 3:
        raise Exception("Invalid input, must be 3 integers separated by space")

    algorithm_code, num_processes, time_slice = [int(x) for x in user_input.split()]

    if algorithm_code == 0:
        algorithm = "FCFS"
        time_slice = 1
    elif algorithm_code == 1:
        algorithm = "SJF"
        time_slice = 1
    elif algorithm_code == 2:
        algorithm = "SRTF"
        time_slice = 1
    elif algorithm_code == 3:
        algorithm = "RR"
    else:
        raise Exception(f"Invalid algorithm code (passed {algorithm_code})")
    
    # Parse input for processes
    processes = []

    for _ in range(num_processes):
        user_input = input()

        if len(user_input.split()) != 3:
            raise Exception("Invalid input, must be 3 integers separated by space")
        
        process_id, arrival_time, burst_time = [int(x) for x in user_input.split()]

        processes.append(Process(process_id, arrival_time, burst_time))

    if algorithm == "FCFS":
        processes = algorithms.fcfs(processes)
    elif algorithm == "SJF":
        processes = algorithms.sjf(processes)
    elif algorithm == "SRTF":
        processes = algorithms.srtf(processes)
    elif algorithm == "RR":
        processes = algorithms.rr(processes, time_slice)

    # Print results
    for process in sorted(processes, key=lambda p: p.id):
        print(process)

    avg_waiting_time = sum([p.waiting_time for p in processes]) / max(len(processes), 1)
    print(f"Average waiting time: {avg_waiting_time:.1f}", end='') # Print without newline


if __name__ == "__main__":
    try:
        run_simulation()
    except Exception as e:
        print(f"ERROR: {e}")