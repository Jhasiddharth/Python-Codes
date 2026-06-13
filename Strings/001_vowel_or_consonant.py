"""
Problem:
Find if the given character is a vowel or consonant.
"""

def is_vowel_or_consonant(char):
    if char in 'aeiouAEIOU':
        return 'Vowel'
    elif char.isalpha():
        return 'Consonant'
    else:
        return 'Invalid input'

# Example usage:
if __name__ == "__main__":
    char = input("Enter a character: ")
    result = is_vowel_or_consonant(char)
    print(f"The character '{char}' is a {result}.")
