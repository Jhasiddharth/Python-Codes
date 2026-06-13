"""
Problem:
Find the sum of all elements in an array.
"""

def sum_of_elements(arr):
    """
    Function to calculate the sum of all elements in an array.

    Parameters:
    arr (list): A list of numbers.

    Returns:
    int/float: The sum of all elements in the array.
    """
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum

# Example usage:
if __name__ == "__main__":
    array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    result = sum_of_elements(array)
    print(f"The sum of elements in the array {array} is: {result}") 
