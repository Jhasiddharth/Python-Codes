"""
Problem:
Find the sum of the numbers in a given range.
"""

def sum_of_numbers_in_range(start, end):
    """
    This function takes two integers, start and end, and returns the sum of all the numbers in that range (inclusive).
    
    Parameters:
    start (int): The starting number of the range.
    end (int): The ending number of the range.
    
    Returns:
    int: The sum of the numbers in the given range.
    """
    total_sum = 0
    for num in range(start, end + 1):
        total_sum += num
    return total_sum
# Example usage:
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
result = sum_of_numbers_in_range(start, end)
print(f"The sum of numbers from {start} to {end} is: {result}")