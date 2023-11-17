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
        if ready_queue:
            process = min(ready_queue, key=lambda x: x.burst_time_remaining)

            # Execute the process
            burst_duration = process.burst(quantum if quantum < process.burst_time_remaining else process.burst_time_remaining)
            current_time += burst_duration
            process.burst_time_remaining -= burst_duration

            # Update the ready queue
            while processes and processes[0].arrival_time <= current_time:
                queue_process = processes.pop(0)
                heapq.heappush(ready_queue, queue_process)

            if process.burst_time_remaining == 0:
                processes_done.append(process)
                ready_queue.remove(process)
            else:
                # Remove and reinsert the process to update its position in the ready queue
                ready_queue.remove(process)
                heapq.heappush(ready_queue, process)
        else:
            current_time += 1

        print(f"Current Time: {current_time}")
        print("Ready Queue:", [p.id for p in ready_queue])
        print("Processes Done:", [p.id for p in processes_done])
        print("===")

    return processes_done

# Test your function
processes = [Process(1, 6, 27), Process(2, 10, 22), Process(3, 13, 20), Process(4, 20, 19), Process(5, 23, 4)]
result = srtf(processes, 2)
print(result)
