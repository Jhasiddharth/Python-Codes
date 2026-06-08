"""
Problem:
Find the reverse of a number.
"""
def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev
# Example usage
number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print(f"The reverse of {number} is {reversed_number}.")
