from factorial import factorial

def permutation(n, r):
    if r > n:
        raise ValueError("r cannot be greater than n")
    return factorial(n) // factorial(n - r)

def combination(n, r):
    if r > n:
        raise ValueError("r cannot be greater than n")
    return factorial(n) // (factorial(r) * factorial(n - r))

# Example usage with given inputs
n = 5
r = 3
print(f"Permutation P({n}, {r}): {permutation(n, r)}")  # Output: 60
print(f"Combination C({n}, {r}): {combination(n, r)}")  # Output: 10