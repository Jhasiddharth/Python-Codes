"""
Problem:
Find the length of a given string without using strlen() function.
"""

def length_of_string(s):
    count = 0
    for char in s:
        count += 1
    return count
# Example usage
input_string = str(input("Enter a string: "))
print(f"The length of the string '{input_string}' is: {length_of_string(input_string)}")