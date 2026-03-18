import functools
import contextvars

# Define a global context variable
request_id = contextvars.ContextVar("request_id", default="N/A")

def with_context(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        rid = request_id.get()
        print(f"[Context: {rid}] → Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Example usage
request_id.set("abc123")

@with_context
def process_data():
    print("Processing data...")

process_data()
# [Context: abc123] → Calling process_data
# Processing data...
