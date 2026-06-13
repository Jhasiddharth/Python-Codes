"""
Problem:
Replace all 0s in a given number with 1s.
"""

def replace_0s_with_1s(num):
    """
    Replaces all 0s in a given number with 1s.

    Args:
    num (int): The input number.

    Returns:
    int: The number with all 0s replaced by 1s.
    """
    # Convert the number to a string to manipulate individual digits
    num_str = str(num)
    
    # Replace all occurrences of '0' with '1'
    modified_num_str = num_str.replace('0', '1')
    
    # Convert the modified string back to an integer
    modified_num = int(modified_num_str)
    
    return modified_num
# Example usage:
input_number = int(input("Enter a number: "))
result = replace_0s_with_1s(input_number)
print(f"Original number: {input_number}, Modified number: {result}")
