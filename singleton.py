import functools

def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Config:
    def __init__(self):
        self.values = {"debug": True}

cfg1 = Config()
cfg2 = Config()
print(cfg1 is cfg2) 
# True
