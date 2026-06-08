"""
Problem:
Find the sum of the n natural numbers.
"""
def sum_of_natural_numbers(n):
    return n * (n + 1) // 2
# Example usage:
n = int(input("Enter a positive integer: "))
result = sum_of_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {result}")
