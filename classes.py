class Process:

    # double underscore to denote "private" class variables
    __id: int
    __arrival_time: int
    __burst_time: int
    
    burst_time_remaining: int

    def __init__(self, id, arrival_time, burst_time) -> None:
        self.__id = id
        self.__arrival_time = arrival_time
        self.__burst_time = burst_time
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
    
    @property
    def waiting_time(self) -> int:
        return self.__burst_time - self.burst_time_remaining
    
    def has_arrived(self, current_time: int) -> bool:
        return current_time >= self.__arrival_time
    
    def __repr__(self) -> str:
        return f"Process(id={self.__id}, arrival_time={self.__arrival_time}, burst_time={self.__burst_time})"


