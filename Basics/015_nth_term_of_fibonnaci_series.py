"""
Problem:
Find the nth term of the Fibonacci series.
"""
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Example usage:
n = int(input("Enter the term number (n) to find in the Fibonacci series: "))
print(f"The {n}th term of the Fibonacci series is: {fibonacci(n)}")
