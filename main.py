# Let's write a program using a for loop to print all numbers from 1 to 10, except multiples of 3:

'''for number in range(1,11):
    if number % 3 ==0:
     continue
    print(number)'''

# Write
# a Python program that takes a positive integer as input from the user and calculates the sum of all numbers from 1 to that input number


def calculate_sum(n):
    total_sum = 0
    for num in range(1, n + 1):
        total_sum += num
    return total_sum

# Input from the user
try:
    number = int(input("Enter a positive integer: "))
    if number <= 0:
        print("Please enter a positive integer.")
    else:
        result = calculate_sum(number)
        print(f"Sum of numbers from 1 to {number} is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
