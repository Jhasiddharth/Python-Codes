"""
Problem:
Find the number of times a digit appears in a given input.
"""

def count_digit_occurrences(n: int, digit: int) -> int:
    """
    Counts the number of times a digit appears in the given number.

    Args:
    n (int): The number in which to count the occurrences of the digit.
    digit (int): The digit to count.

    Returns:
    int: The number of times the digit appears in the number.
    """
    # Convert the number to a string to iterate through its digits
    n_str = str(n)
    
    # Count the occurrences of the digit in the string representation of the number
    count = n_str.count(str(digit))
    
    return count
# Example usage:
number = int(input("Enter a number: "))
digit_to_count = int(input("Enter the digit to count: "))
result = count_digit_occurrences(number, digit_to_count)
print(f"The digit {digit_to_count} appears {result} times in the number {number}.")



