"""
Problem:
Binary to Decimal Conversion: Write a function that takes a binary number as input and converts it to its decimal equivalent.
"""

def binary_to_decimal(binary_str):
    decimal_value = 0
    power = 0
    
    # Reverse the binary string to process from the least significant bit
    binary_str = binary_str[::-1]
    
    for digit in binary_str:
        if digit == '1':
            decimal_value += 2 ** power
        power += 1
        
    return decimal_value
# Example usage:
binary_number = input('Enter a binary number: ')
decimal_number = binary_to_decimal(binary_number)
print(f"The decimal equivalent of binary {binary_number} is {decimal_number}.")
