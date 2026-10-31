# Made by: GUILLAUME AMORIM
# 10/31/2026
# Class: Introduction to programming COSC1100
# Assignment 1: Square Numbers – Iteration

# CITATIONS and AI use: 
# Claude (by Anthropic) was used to review the code.
# Claude suggested using constants instead typing the fixed numbers directly into the code, and adding empty print() statements for spacing.
# The planning process, program logic and deskcheck are my own and made with the help of previous in class activities and class resources.

# THE PROGRAM REQUIREMENTS:
# For this lab you will create a simple console application using Python that will graphically display all the square
# numbers within a range provided by the user. For our purposes, a square number is any number that can be
# computed by multiplying a whole number by itself. The first several square numbers are 1 (1 squared), 4 (2
# squared), 9 (3 squared) and 16 (4 squared). This assignment will provide you with the opportunity to design
# program logic with both individual and nested loops. It should also reinforce the time-saving value of planning
# before you code.

# INPUTS:
# Lower limit: prompt user for a whole number between the range of 1 and 10,000 inclusive
# Upper limit: prompt user for a whole number between the lower limit entered and 10,000 inclusive
# User input must be numeric and whole, no processing until user input is valid
# Invalid user input will prompt an error message and loop until condition is met

# PLAN(PSEUDOCODE):
# 0. Define constants
#    -Minimum input limit and maximum input limit
#    -Minimum square root and maximum square root
# 1. Display a banner-like header with "square number finder" written inside
# 2. Use a while loop to validate the user input and prompt the error message for the lower bound limit
#    -I will want to validate user input is a integer and within the range of 1 and 10000 inclusive
# 3. Use a while loop to validate the user input and prompt the error message for the upper bound limit
#    -I will want to validate user input is a integer and within the range of the lower limit and 10000 inclusive
# 4. Display results banner with previously entered lower and upper limit
# 5. Using a for loop, calculate all square numbers and its square root within the user range under a banner
#    -The square numbers will be 1 to 10000 and the square root will fall under 1 to 100
#    -In order for the range to actually land at 100, I will use range(1, 100 + 1)
#    -To get each square number, I will multiply the root by itself
# 6. At the end, use input() to allow program to pause and user to input(Enter), to exit

# OUTPUTS:
# Output will show the square number and square root of the number within the range of the user input entered under a banner

# PROGRAM:
# Constants:
MIN_LIMIT = 1
MAX_LIMIT = 10000
MIN_SQUARE_ROOT = 1
MAX_SQUARE_ROOT = 100

# 1.Banner:
print("*************************************************************************************")
print("                             SQUARE NUMBER FINDER")
print("*************************************************************************************")
print()

# 2.Lower limit:
is_valid_lower = False

while is_valid_lower != True:
    lower_limit_input = input("Please enter the lower bound: ")
    if lower_limit_input.isdigit():
        lower_limit = int(lower_limit_input)
        if lower_limit >= MIN_LIMIT and lower_limit <= MAX_LIMIT:
            is_valid_lower = True
        else:
            print(f"Invalid input: Please enter a number between {MIN_LIMIT} and {MAX_LIMIT}.")
            print()
    else:
        print("Invalid input: Please enter a whole number.")
        print()

# 3.Upper limit:
is_valid_upper = False

while is_valid_upper != True:
    upper_limit_input = input("Please enter the upper bound: ")
    if upper_limit_input.isdigit():
        upper_limit = int(upper_limit_input)
        if upper_limit >= lower_limit and upper_limit <= MAX_LIMIT:
            is_valid_upper = True
        else:
            print(f"Invalid input: Please enter a number between {lower_limit} and {MAX_LIMIT}.")
            print()
    else:
        print("Invalid input: Please enter a whole number.")
        print()

# 4.Display results banner:
print("*************************************************************************************")
print(f"                         Square Numbers Between {lower_limit} and {upper_limit}")
print("*************************************************************************************")

# 5.Calculate square numbers:
for root in range(MIN_SQUARE_ROOT, MAX_SQUARE_ROOT + 1):
    square = root * root
    if square >= lower_limit and square <= upper_limit:
        print(f"{square} ({root} squared)")

# 6.Pause program using input():
input("Press Enter to exit program")

# DESKCHECK:
# I make sure the validations are correct for lower bound:
# -if I enter chicken, I get: Invalid input: Please enter a whole number.
# -if I enter 4.5, I get: Invalid input: Please enter a whole number.
# -if I enter a number outside of the range, I get: Invalid input: Please enter a number between 1 and 10000.
# I make sure the validations are correct for upper bound:
# -if I enter 10001 for the upper bound, I get: Invalid input: Please enter a number between 10 and 10000.
# -if I enter a number below the previous lower bound input of 10, I get: Invalid input: Please enter a number between 10 and 10000.
# -if I input 100 after the previous input of 10, I should get a range from 10 to 100, and the square roots, I get:
# *************************************************************************************
#                          Square Numbers Between 10 and 100
# *************************************************************************************
# 16 (4 squared)
# 25 (5 squared)
# 36 (6 squared)
# 49 (7 squared)
# 64 (8 squared)
# 81 (9 squared)
# 100 (10 squared)
# Press Enter to exit program