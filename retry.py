import functools
import random
import time


def retry(retries=3, delay=0.5, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying...")
                    time.sleep(delay)

        return wrapper

    return decorator


@retry(retries=5, delay=1)
def unstable_call():
    if random.random() < 0.8:
        raise ConnectionError("Connection dropped")
    return "Success!"


print(unstable_call())
# Attempt 1 failed: Connection dropped. Retrying...
# Attempt 2 failed: Connection dropped. Retrying...
# Success!
