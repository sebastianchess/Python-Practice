from typing import Literal
from collections.abc import Iterator


type BinaryType = Literal[0, 1]


class Binary:
    """Binary Number Handler"""
    def __init__(self, *args: BinaryType) -> None: 
        self._current = 0

        if not args:
            raise Exception("Not Empty")
        
        if len(args) > 8: 
            self._args = args[:9]
        
        elif len(args) < 8:
            filled_zeros: tuple[BinaryType, ...] = (0,) * (8 - len(args))
            self._args = filled_zeros + args
        else:
            self._args = args
    
    def decimal(self) -> int:
        """Converts a binary number to decimal"""
        new = 0 

        for pos, el in enumerate(self._args[::-1]):
            new += el * (2**pos)
        
        return new
    
    @classmethod
    def from_int[T](cls: type[T], decimal: int) -> T:
        """Creates a Binary object from a decimal.
        
        Attributes
        ----------
        decimal : `builtins.int`
            the decimal to be converted to Binary.
        
        Example
        -------
        ```
        eleven = Binary.from_int(11)
        print(eleven) # 00001011
        ```

        Returns
        -------
        `Binary`
            The instance of `Binary` type.
        
        """
        return cls(*map(int, bin(decimal)[2:].zfill(8)))
    
    def __add__(self, other: "Binary") -> "Binary": 
        return Binary(1)

    def __str__(self) -> str: 
        return ''.join(str(b) for b in self)

    def __repr__(self) -> str: 
        return f"Binary({''.join(str(b) for b in self)})"
    
    def __len__(self) -> int: 
        return len(self._args)

    def __iter__(self) -> Iterator[BinaryType]:
        self._current = 0 
        return self 

    def __next__(self) -> BinaryType:
        if self._current == len(self):
            raise StopIteration
        
        value = self._args[self._current]
        self._current += 1

        return value 

one = Binary.from_int(1) 
print(one)
