from functools import lru_cache
import time

@lru_cache(maxsize=5)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
start = time.time()
fibonacci(30)
end = time.time()
print("Time with lru_cache(maxsize=5):", end - start)
def fibonacci_no_cache(n):
    if n <= 1:
        return n
    return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)
start = time.time()
fibonacci_no_cache(30)
end = time.time()
print("Time without lru_cache:", end - start)