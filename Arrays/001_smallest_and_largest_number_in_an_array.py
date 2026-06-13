"""
Problem:
Find the smallest and largest numbers in a given array.
"""

def find_smallest_and_largest(arr):
    if not arr:
        return None, None  # Return None for both if the array is empty

    smallest = largest = arr[0]  # Initialize smallest and largest with the first element

    for num in arr:
        if num < smallest:
            smallest = num  # Update smallest if current number is smaller
        elif num > largest:
            largest = num  # Update largest if current number is larger

    return smallest, largest  # Return the smallest and largest numbers

# Example usage:
if __name__ == "__main__":
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    smallest, largest = find_smallest_and_largest(array)
    print(f"Smallest number: {smallest}, Largest number: {largest}")

