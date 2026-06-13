"""
Problem:
Reverse an array.
"""


def reverse_array(arr):
    return arr[::-1]

# Example usage:
if __name__ == "__main__":
    array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    reversed_array = reverse_array(array)
    print(f"The reversed array is: {reversed_array}")
