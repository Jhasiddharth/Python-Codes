"""
Problem:
Find the number of digits in a given integer.
"""

def count_digits(n):
    """
    Counts the number of digits in the given integer n.

    Parameters:
    n (int): The integer whose digits are to be counted.

    Returns:
    int: The number of digits in the integer n.
    """
    # Convert the integer to a string and count its length
    return len(str(abs(n)))
# Example usage:
number = int(input("Enter an integer: "))
print(f"The number of digits in {number} is: {count_digits(number)}")


