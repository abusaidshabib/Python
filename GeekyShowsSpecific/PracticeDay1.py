
# ------ Write a simple program that prints "Hello, World!" to the console. -----------

# print("Hello, World!")

# ------ Create a program that calculates the area of a rectangle. You should prompt the user for the length and width. -----------
# import math

# height = float(input("Enter the height of rectangle?"))
# width = float(input("Enter the width of rectangle?"))
# print(height, width)
# result = height * width
# print(result)

# ------ Write a program that finds and prints the sum of all even numbers in a list. -----------
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# result = 0
# for number in numbers:
#     if number % 2 == 0:
#         result += number

# print(result)

#--------- Create a program that reverses a user-inputted string. -------------------
# result = input("Enter a string")
# print(result[::-1])

#------------- Write a program that determines whether a number entered by the user is positive, negative, or zero. -----------------
# value = float(input("Enter a number: "))
# if value < 0:
#     print("This is a negative number")
# elif value > 0:
#     print("This is a positive number")
# else:
#     print("This is zero")

#------------- Define a function that checks if a number is prime. ---------------------------------
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# number_to_check = int(input("Enter a number to check for primality: "))
# if is_prime(number_to_check):
#     print("Prime number")
# else:
#     print("Not a prime number")

#-------------- Create a program that counts the frequency of each letter in a user-inputted string and stores the result in a dictionary.--------------------
# user_input = input("Enter a string: ")

# letter_frequency = {}
# for char in user_input:
#     if char.isalpha():
#         char_lower = char.lower()
#         letter_frequency[char_lower] = letter_frequency.get(char_lower, 0) + 1

# print("Letter frequency:", letter_frequency)