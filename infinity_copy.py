from __future__ import annotations

from typing import Any, Literal

class _InfType:
    """Python Infinity Remake"""
    __slots__ = ("_negative",)

    def __init__(self): 
        self._negative = False
 
    def __neg__(self):
        new = _InfType()
        new._negative = not self._negative
        return new

    def __gt__(self, other: Any): 
        if self._negative:
            return False 
        return True 

    def __lt__(self, other: Any): 
        if self._negative: 
            return True 
        return False 

    def __bool__(self) -> Literal[True]: 
        """Always Returns True"""
        return True
    
    def __eq__(self, value: Any | _InfType) -> bool:
        return isinstance(value, _InfType) and self._negative == value._negative

    def __add__(self, other: Any | _InfType): 
        if isinstance(other, _InfType):
            if self == other: 
                return self 
            return "nan"
        return self 
    
    def __radd__(self, other: Any | _InfType):
        return self.__add__(other)

    def __mul__(self, other: Any | _InfType):
        new_ = _InfType()

        if isinstance(other, int): 
            
            if other == 0: 
                return "nan"
            
            new_._negative = self._negative ^ [False, True][other < 0]
            return new_
        
        new_._negative = self._negative ^ other._negative
        return new_ 
    
    def __rmul__(self, other: Any | _InfType):
        return self.__mul__(other)
    
    def __div__(self, other: Any | _InfType):
        ... 
    
    def __rdiv__(self, other: Any | _InfType):
        ...
    
    def __divmod__(self, other: Any | _InfType): 
        ...

    def __rdivmod__(self, other: Any | _InfType):
        ...

    def __repr__(self) -> str:
        return f"{'-' * self._negative}inf"


inf = _InfType() 

print(inf > 2)
print(-inf < -10)
