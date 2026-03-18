import time
import functools

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"{func.__name__} executed in {elapsed:.2f} ms")
        return result
    return wrapper

@timeit
def compute(n):
    return sum(range(n))

compute(10_000_000)
# compute executed in 71.61 ms
