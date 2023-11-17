from classes import Process
import heapq
from typing import List

def srtf(processes: List[Process], quantum: int) -> List[Process]:
    processes.sort(key=lambda process: process.arrival_time)

    processes_done = []
    ready_queue: List[Process] = []

    # Initialize ready queue with the first process
    ready_queue.append(processes.pop(0))
    current_time = ready_queue[0].arrival_time

    while len(processes) > 0 or len(ready_queue) > 0:
        # Get the process with the minimum remaining burst time from the ready queue
        process = min(ready_queue, key=lambda x: x.burst_time_remaining)

        # Simulate burst
        burst_duration = process.burst(quantum)
        current_time += burst_duration

        # Update ready queue
        while processes:
            if len(ready_queue) == 0:
                # If the queue is empty, move the process with the earliest arrival time to the ready queue
                queue_process = processes.pop(0)
                current_time = max(current_time, queue_process.arrival_time)
                ready_queue.append(queue_process)

            elif processes[0].has_arrived(current_time):
                queue_process = processes.pop(0)
                ready_queue.append(queue_process)

            else:
                break

        # Move process to the ready queue/finished list
        if process.burst_time_remaining > 0:
            ready_queue.remove(process)
            ready_queue.append(process)
        else:
            processes_done.append(process)
            ready_queue.remove(process)

        print(f"Current Time: {current_time}")
        print("Ready Queue:", [p.id for p in ready_queue])
        print("Processes Done:", [p.id for p in processes_done])
        print("===")

    # Calculate average waiting time after the while loop
    total_waiting_time = sum(process.waiting_time for process in processes_done)
    average_waiting_time = total_waiting_time / len(processes_done) if processes_done else 0.0
    print("Average Waiting Time:", average_waiting_time)

    return processes_done

# Test your function
processes = [Process(2, 5, 29), Process(1, 6, 27), Process(2, 10, 22), Process(3, 13, 20), Process(4, 20, 19), Process(5, 23, 4)]
result = srtf(processes, 2)
print(result)
