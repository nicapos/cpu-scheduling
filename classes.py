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
    
    def burst(self, current_time: int) -> int:
        """ Simulates burst, returns the burst time (for current burst) """
        current_burst_time = self.burst_time

        if self.burst_time_remaining > 0:
            if self.burst_time_remaining > self.burst_time:
                self.burst_time_remaining -= self.burst_time
                
            else: # Process will finish in this burst
                current_burst_time = self.burst_time_remaining
                self.burst_time_remaining = 0

                completion_time = current_time + self.burst_time
                turnaround_time = completion_time - self.__arrival_time
                self.waiting_time = turnaround_time - self.burst_time
                # SIMPLIFIED: self.waiting_time = current_time - self.__arrival_time

        self.start_times.append(current_time)
        self.end_times.append(current_time + current_burst_time)

        return current_burst_time
    
    def burst_partial(self, current_time: int, burst_time: int) -> int:
        pass    # TODO: Implement this for SRTF and RR

    def __str__(self) -> str:
        bursts = []
        for start_time, end_time in zip(self.start_times, self.end_times):
            bursts.append(f"start time: {start_time} end time: {end_time}")

        return f"{self.__id} {' | '.join(bursts)} | Waiting time: {self.waiting_time}"
    
    def __repr__(self) -> str:
        # For debugging only
        return f"Process(id={self.__id}, arrival_time={self.__arrival_time}, burst_time={self.__burst_time})"
