import time

def debug(func):
    def wrapper(*args, **kwargs):
        arg_value=', '.join(str(arg) for arg in args)
        kwarg_value=', '.join(f"{k} : {v}" for k, v in kwargs.items())
        print(f"calling {func.__name__} with args {arg_value} with kwargs {kwarg_value}")
        return func(*args, **kwargs)
    
    return wrapper  


@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Guneet", greeting="Welcome")