import time
def LOG(log_level):
    def log_func(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            res = func(*args, **kwargs)
            end_time = time.perf_counter()
            Itog = end_time - start_time
            print(f'{log_level}: {func.__name__} was called! for time: {Itog:.6f} seconds')
            return res
        return wrapper
    return log_func

@LOG("INFO")
def add(x, y):
    time.sleep(1)
    return x + y
result = add(5, 7)
print(result)