import functools

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with {args=} {kwargs=}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result!r}")
        return result
    return wrapper

@log_call
def greet(name):
    return f"Hello, {name}!"

greet("Alice")
# [LOG] Calling greet with args=('Alice',) kwargs={}
# [LOG] greet returned 'Hello, Alice!'
