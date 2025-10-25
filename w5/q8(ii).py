from functools import lru_cache

@lru_cache(maxsize=5)
def fibonacci(n):
    """This function outputs the sum of n Fibonacci numbers"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci.__doc__)