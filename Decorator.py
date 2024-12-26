def run(times):
    def deco(func):
        def wrapper(*args, **kwargs):
            (func(*args, **kwargs) for _ in times)
        return wrapper 
    return deco 


def add(func):
    def wrapper(*args):
        value = func(*args)

        if isinstance(value, str):
            return value + "Hello"
        
        if isinstance(value, int):
            return value + 1 
        
        return value 
    return wrapper 

@run(10)
def func():
    print("hello")

@add
def func_2():
    return "test"

func() # It'll call this function 10 times.
##################################################################

print(func_2()) # testHello

@add
def add_numbers(a, b):
    return a + b 

print(add_numbers(1, 3)) # 5 


