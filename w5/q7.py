import time
def log_time(func):
    def wrapper(n):
        start = time.time()
        result = func(n)
        end = time.time()
        print(f"{func.__name__}({n}) took {end - start:.6f} seconds")
        return result
    return wrapper
@log_time
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))