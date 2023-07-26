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

    '''Let say we want to write a program that checks if a given number is positive, negative, or zero.'''

    Number = int(input("Please enter the number:"))
    print("You have Enter this:", Number)
    if Number > 0:

        print("this number is Positive Number")
        # if Number==2:
        #     print ("it is even number")
        # else :
        #     print(("It is Odd Number"))

    elif Number < 0:

        print("This Number is Negative")
    else:
        print("Number is Zero ")

    '''def check_number(n):
        if n > 0:
            print("The number is positive.")
        elif n < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")

    # Test the function
    number = int(input("Enter a number: "))
    check_number(number)
    '''


