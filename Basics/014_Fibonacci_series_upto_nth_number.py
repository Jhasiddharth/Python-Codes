"""
Problem:
Find the Fibonacci series until the number input as the Nth term.
"""
def fibonacci_series(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1
n = int(input("Enter the number of terms: "))
print("Fibonacci series:")
fibonacci_series(n)
