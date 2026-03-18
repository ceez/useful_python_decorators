import functools
import time
import types


def time_methods(cls):
    for name, attr in list(cls.__dict__.items()):
        if isinstance(attr, (types.FunctionType, types.MethodType)):

            @functools.wraps(attr)
            def wrapper(self, *args, __orig=attr, **kwargs):
                start = time.perf_counter()
                result = __orig(self, *args, **kwargs)
                elapsed = (time.perf_counter() - start) * 1000
                print(f"{cls.__name__}.{__orig.__name__} took {elapsed:.2f} ms")
                return result

            setattr(cls, name, wrapper)
    return cls


@time_methods
class Processor:
    def task_one(self):
        time.sleep(0.02)

    def task_two(self, n):
        return sum(range(n))


p = Processor()
p.task_one()
p.task_two(100_000)
# Processor.task_one took 25.03 ms
# Processor.task_two took 0.80 ms
