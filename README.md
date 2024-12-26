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




