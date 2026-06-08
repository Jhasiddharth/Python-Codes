"""
Problem:
Find the greatest of two numbers.
"""
def greatest_of_two_numbers(a, b):
    if a > b:
        return a
    else:
        return b
# Example usage:
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = greatest_of_two_numbers(a, b)
print(f"The greatest of {a} and {b} is: {result}")