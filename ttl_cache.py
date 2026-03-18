import functools
import time

def ttl_cache(ttl_seconds):
    cache = {}
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            now = time.time()
            if args in cache:
                value, timestamp = cache[args]
                if now - timestamp < ttl_seconds:
                    return value
            result = func(*args)
            cache[args] = (result, now)
            return result
        return wrapper
    return decorator

@ttl_cache(ttl_seconds=3)
def expensive(x):
    print("Computing...")
    return x * x

print("First call:")
expensive(4)
print("\nSecond call:")
time.sleep(1)
expensive(4) # served from cache
print("\nThird call:")
time.sleep(4)
expensive(4) # recomputed after TTL expiry
# First call:
# Computing...
# Second call:
# Served from cache
# Third call:
# Computing...
