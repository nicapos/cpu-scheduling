from classes import Process


def fcfs(processes: list[Process]) -> list[Process]:
    processes.sort(key=lambda process: process.arrival_time)

    current_time = 0

    for next_process in processes:
        current_time = max(current_time, next_process.arrival_time)

        next_process.burst(current_time)
        current_time += next_process.burst_time

    return processes

