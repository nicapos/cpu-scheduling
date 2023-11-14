from classes import Process


def fcfs(processes: list[Process]) -> list[Process]:
    processes.sort(key=lambda process: process.arrival_time)

    current_time = 0

    for next_process in processes:
        current_time = max(current_time, next_process.arrival_time)

        next_process.burst(current_time)
        current_time += next_process.burst_time

    return processes

def sjf(processes: list[Process]) -> list[Process]:
    pass    # TODO: Implement this


def srtf(processes: list[Process]) -> list[Process]:
    pass    # TODO: Implement this


def rr(processes: list[Process], quantum: int) -> list[Process]:
    processes.sort(key=lambda process: process.arrival_time)

    processes_done = []
    ready_queue: list[Process] = []

    # Initialize ready queue with first process
    ready_queue.append(processes.pop(0))
    current_time = ready_queue[0].arrival_time

    while len(processes) > 0 or len(ready_queue) > 0:
        # Get next process from ready queue
        process = ready_queue.pop(0)

        # Simulate burst
        burst_duration = process.burst(current_time, quantum)
        current_time += burst_duration

        # Update ready queue
        while processes:
            if len(ready_queue) == 0:
                # If queue is empty, move process with earliest arrival time to ready queue
                queue_process = processes.pop(0)
                current_time = max(current_time, process.arrival_time)
                ready_queue.append(queue_process)

            elif processes[0].has_arrived(current_time):
                queue_process = processes.pop(0)
                ready_queue.append(queue_process)

            else:
                break

        # Move process to ready queue/finished list
        if process.burst_time_remaining > 0:
            ready_queue.append(process)
        else:
            processes_done.append(process)

    return processes_done


# Long version of FCFS. Can be used as a reference for the other algorithms
def _fcfs(processes: list[Process]) -> list[Process]:
    processes.sort(key=lambda process: process.arrival_time)

    processes_done = []
    ready_queue: list[Process] = []

    current_time = 0

    for _ in range(len(processes)): # O(n)
        # Update ready queue
        while processes:
            if len(ready_queue) == 0:
                # If queue is empty, move process with earliest arrival time to ready queue
                process = processes.pop(0)
                current_time = max(current_time, process.arrival_time)
                ready_queue.append(process)

            elif processes[0].has_arrived(current_time):
                process = processes.pop(0)
                ready_queue.append(process)

            else:
                break

        # Get next process from ready queue
        process = ready_queue.pop(0)

        # Simulate burst
        burst_duration = process.burst(current_time)
        current_time += burst_duration

        # Move process to ready queue/finished list
        if process.burst_time_remaining > 0:
            ready_queue.append(process)
        else:
            processes_done.append(process)

    return processes_done
