class Process:

    # double underscore to denote "private" class variables
    __id: int
    __arrival_time: int
    __burst_time: int

    burst_time_remaining: int
    waiting_time = 0

    start_times: list[int]
    end_times: list[int]

    def __init__(self, id, arrival_time, burst_time) -> None:
        self.__id = id
        self.__arrival_time = arrival_time
        self.__burst_time = burst_time

        self.start_times = []
        self.end_times = []
        self.burst_time_remaining = burst_time

    # getters
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def arrival_time(self) -> int:
        return self.__arrival_time
    
    @property
    def burst_time(self) -> int:
        return self.__burst_time
    
    def has_arrived(self, current_time: int) -> bool:
        return current_time >= self.__arrival_time
    
    def burst(self, current_time: int, partial_burst_time: int = None) -> int:
        if partial_burst_time is None:
            return self.__burst(current_time, self.burst_time)
        return self.__burst(current_time, partial_burst_time)
    
    def __burst(self, current_time: int, burst_time: int) -> int:
        """ Simulates burst, returns the burst time (for current burst) """
        current_burst_time = min(burst_time, self.burst_time_remaining)
        self.burst_time_remaining -= current_burst_time

        # Update waiting time
        if self.start_times:
            self.waiting_time += current_time - self.end_times[-1]
        else:
            self.waiting_time += current_time - self.arrival_time

        # Check if previous burst is the same as this burst's start
        if self.end_times and self.end_times[-1] == current_time:
            # In this case, extend the previous burst
            self.end_times.pop()
            self.end_times.append(current_time + current_burst_time)
        else:
            self.start_times.append(current_time)
            self.end_times.append(current_time + current_burst_time)
        
        return current_burst_time

    def __str__(self) -> str:
        bursts = []
        for start_time, end_time in zip(self.start_times, self.end_times):
            bursts.append(f"start time: {start_time} end time: {end_time}")

        return f"{self.__id} {' | '.join(bursts)} | Waiting time: {self.waiting_time}"
    
    def __repr__(self) -> str:
        # For debugging only
        return f"Process(id={self.__id}, arrival_time={self.__arrival_time}, burst_time={self.__burst_time})"
    
    def __lt__(self, other):
        return self.burst_time_remaining < other.burst_time_remaining
