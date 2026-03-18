import functools

def inject(**services):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Inject services as local variables
            func.__globals__.update(services)
            return func(*args, **kwargs)
        return wrapper
    return decorator

logger = lambda msg: print(f"[LOG]: {msg}")
validator = lambda x: len(x) > 0

@inject(logger=logger, validator=validator)
def process_data(data):
    logger(f"Processing {data}...")
    if validator(data):
        print(data.upper())
    return None

process_data("Yang Zhou")
# [LOG]: Processing Yang Zhou...
# YANG ZHOU
