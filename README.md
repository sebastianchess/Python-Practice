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
























