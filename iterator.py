from typing import TypedDict, Unpack, NotRequired
from collections.abc import Iterator 


class _RangeTyped(TypedDict):
    start: NotRequired[int]
    stop: NotRequired[int]
    step: NotRequired[int]


class Range:
    """built-in range copy"""
    def __init__(self, *args: int, **kwargs: Unpack[_RangeTyped]) -> None:

        if args: 
            if len(args) == 1:
                self.start, self.stop, self.step = 0, args[0], 1

            elif len(args) == 2:
                self.start, self.stop, self.step = args[0], args[1], 1
            
            elif len(args) == 3:
                self.start, self.stop, self.step = *args,
            else:
                raise Exception 
            return 

        elif kwargs: 
            self.start = kwargs.get("start", 0)
            self.stop = kwargs["stop"] # type: ignore
            self.step = kwargs.get("step", 1)
        else:
            raise Exception("Params missed")
        
        self._counter = 0

    def __iter__(self) -> Iterator: 
        self._counter = self.start - 1
        return self 

    def __next__(self) -> int: 

        if self._counter == self.stop - 1 or self._counter + self.step >= self.stop:
            raise StopIteration
        
        self._counter += self.step
        return self._counter

