"""
Problem:
Find the sum of digits of a given number.
"""
def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total
# Example usage:
number = int(input("Enter a number: "))
print(f"The sum of digits of {number} is {sum_of_digits(number)}.")