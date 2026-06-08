"""
Problem:
Find the sum of the first n natural numbers.
"""

num = int(input("Enter a number: "))
#sum_of_natural_numbers = num * (num + 1) // 2  #Through formula: n(n+1)/2
#print("The sum of the first", num, "natural numbers is:", sum_of_natural_numbers)

# Alternative method using a loop
if num <= 0:
    print("Please enter a positive number.")
else:
    total_sum = 0

    for i in range(1, num + 1):
        total_sum += i

    print("The sum of the first", num, "natural numbers is:", total_sum)
