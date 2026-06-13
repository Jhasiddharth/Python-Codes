"""
Problem:
Find the repeating elements in an array of integers.
"""


def find_repeating_elements(arr):
    seen = set()
    repeating = set()
    for num in arr:
        if num in seen:
            repeating.add(num)
        else:
            seen.add(num)
    return list(repeating)

# Example usage:
if __name__ == "__main__":
    array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    repeating_elements = find_repeating_elements(array)
    print(f"The repeating elements in the array {array} are: {repeating_elements}")
