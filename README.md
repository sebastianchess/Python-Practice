# Iterator
I'm not really experienced with Iterators. I'd say this is my first time implementing them in senseful code. Well in this code I am making a replicate of `builtins.range` type. To summarize the explanation, Iterables are objects you can loop through. Iterators are objects (classes) that contains `__next__` and `__iter__` (obviously). Not all Iterables are Iterators, for example `builtins.list` you can loop through it, but it doesn't use `__next__`.

**Simple Implementation**

```py
class IteratorClass:
    def __init__(self, limit):
        self.limit = limit 
        self.counter = 0

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == self.limit:
            raise StopIteration
        self.counter += 1
        return self.counter

obj = IteratorClass(10)

for i in obj: print(i)
```
When you loop through it, it will first call `__iter__` and set the counter to where it's supposed to start at (0). Then since it returns the instance itself which is an iterator, this will call `next` N times until `self.counter` becomes the limit number we passed. 


# Decorators

### Explanation:
Decorators are functions that modify the functionality of other functions. They are used in the following syntax:
```py
@the_decorator
def function(): ...
```
Note that `@the_decorator` means that the function we created `function` will be passed to `the_decorator` function in parameters, which means `function` will stop being the function itself but the value returned by `the_decorator`, meaning:
```py
function = the_decorator(function)
```

### Example
```py
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before func was called")
        func(*args, **kwargs)
        print("After it was called")
    return wrapper

@decorator
def message():
    print("Hello World")
```
So when you do `message()` you'd actually be calling `wrapper`.

There are also decorators that receive arguments
### Example
```py
def whatever(name=None):
    def deco(func):
        def wrap():
            print("hello ", name)
            func()
        return wrap 
    return deco 

@whatever("sebastian")
def func():
    return None 

func() # Hello  sebastian
```
I accept the fact it's not a good example. But in the decorator, this would be equivalent to.
```py
def func():
    return None

func = whatever("sebastian")(func) 
```
I hope you understood how decorators work!.
























