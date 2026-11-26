def factorial_iterative(n):
    """Calculates factorial using a loop (Iterative approach)."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """Calculates factorial by calling itself (Recursive approach)."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


num = 5

print(f"Iterative method output for {num}! is: {factorial_iterative(num)}")
print(f"Recursive method output for {num}! is: {factorial_recursive(num)}")
