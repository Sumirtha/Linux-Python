from datetime import datetime
def log_time(func):
    def wrapper(*args, **kwargs):
        entry_time = datetime.now()
        print(f"Entering {func.__name__} with args {args} at {entry_time}")
        result = func(*args, **kwargs)
        exit_time = datetime.now()
        print(f"Exiting {func.__name__} with args {args} at {exit_time}")
        return result
    return wrapper
@log_time
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci(5)