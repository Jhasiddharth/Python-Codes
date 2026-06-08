"""
Problem:
Find the sum of the first n natural numbers.
"""

num = int(input("Enter a number: "))
#sum_of_natural_numbers = num * (num + 1) // 2  #Through formula: n(n+1)/2
#print("The sum of the first", num, "natural numbers is:", sum_of_natural_numbers)

# Alternative method using a loop
sum_of_natural_numbers_loop = 0
for i in range(1, num + 1):
    sum_of_natural_numbers_loop += i
print("The sum of the first", num, "natural numbers using loop is:", sum_of_natural_numbers_loop)
