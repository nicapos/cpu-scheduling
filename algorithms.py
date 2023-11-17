from classes import Process
import heapq

def fcfs(processes: list[Process]) -> list[Process]:
    processes.sort(key=lambda process: process.arrival_time)

    current_time = 0

    for next_process in processes:
        current_time = max(current_time, next_process.arrival_time)

        next_process.burst(current_time)
        current_time += next_process.burst_time

    return processes

def sjf(processes: list[Process]) -> list[Process]:
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
        sj_index = min(range(len(ready_queue)), key=lambda i: ready_queue[i].burst_time) # get the index of the shortest job
        process = ready_queue.pop(sj_index)
    
        # Simulate burst
        burst_duration = process.burst(current_time)
        current_time += burst_duration

        # Move process to ready queue/finished list
        if process.burst_time_remaining > 0:
            ready_queue.append(process)
        else:
            processes_done.append(process)
        
    return processes_done
     


def srtf(processes: list[Process]) -> list[Process]:
    time = 0
    total_wait = 0
    pl = list(processes)
    arrival_queue = heapq.createHeap(len(processes), "ARRIVAL") 
    ready_queue = heapq.createHeap(pl.size, "BURST")

    if arrival_queue is None or ready_queue is None:
        print("Error: Unable to allocate")
        return

    for i in range(pl.size):
        heapq.insertHeap(arrival_queue, pl.processes[i])

    preempt = 0
    running = None

    while arrival_queue.size > 0 or ready_queue.size > 0:
        while heapq.peekHeap(arrival_queue) is not None and heapq.peekHeap(arrival_queue).arrival_time <= time:
            heapq.insertHeap(ready_queue, heapq.extractMin(arrival_queue))
            preempt = 1

        if ready_queue.size == 0:
            time = heapq.peekHeap(arrival_queue).arrival_time if heapq.peekHeap(arrival_queue) is not None else time
            continue

        if preempt == 1:
            min_process = heapq.peekHeap(ready_queue)
            if running is None or running.pid != min_process.pid:
                heapq.appendStartTime(min_process, time)
            if running is not None and running.pid != min_process.pid:
                heapq.appendEndTime(running, time)
            running = min_process
            preempt = 0

        time += 1
        running.remaining_burst -= 1

        if running.remaining_burst == 0:
            running = None
            preempt = 1
            # Compute wait time of completed process
            completed = heapq.extractMin(ready_queue)
            heapq.appendEndTime(completed, time)
            turnaround = time - completed.arrival_time
            completed.waiting_time = turnaround - completed.burst_time
            total_wait += completed.waiting_time

    pl.ave_wait_time = total_wait / pl.size
    heapq.freeHeap(ready_queue)
    heapq.freeHeap(arrival_queue)


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
