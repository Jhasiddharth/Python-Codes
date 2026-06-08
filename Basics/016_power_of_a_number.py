"""
Problem:
Find the power of a number.
"""
def power(base, exponent):
    """
    Calculate the power of a number.

    Parameters:
    base (float): The base number.
    exponent (int): The exponent to which the base is raised.

    Returns:
    float: The result of base raised to the power of exponent.
    """
    return base ** exponent
# Example usage:
if __name__ == "__main__":
    base = float(input("Enter the base number: "))
    exponent = int(input("Enter the exponent: "))
    result = power(base, exponent)
    print(f"{base} raised to the power of {exponent} is {result}.")
