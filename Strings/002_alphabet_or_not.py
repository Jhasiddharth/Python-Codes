"""
Problem:
Find if the given character is alphabet or not.
"""
def is_alphabet(char):
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        return True
    else:
        return False

alphabet = input("Enter a character: ")
if is_alphabet(alphabet):
    print(f"{alphabet} is an alphabet.")
else:
    print(f"{alphabet} is not an alphabet.")
