# Made by: Guillaume Amorim
# 11/6/2026
# Class: Intro to programming, COSC1100
# In class activity: Arrays

# THE PROBLEM:
# Write a program to calculate your midterm mark. The description on how your
# midterm mark was calculated is in the course outline. Please refer back to the
# course outline for details.
# Your program must ask the user for their marks for each assessment, ordered by
# type. The assessments include the Pre-Class Activities, Class Exercises, the first
# Test. Once the user finishes their entry, calculate and display the user’s grade as
# a percentage and their percentage for each type of assessment.
# Your user may not always enter the correct details when asked. Ensure your
# program can identify that and guide the user on entering valid data

# INPUTS:
# In class activities (Planning, Numeric, Selection, Iteration) = whole number 0-100 for each
# Assignment 1 = whole number 0-100
# Test 1 = whole number 0-100

# OUTPUTS: 
# Output will be the final calculated percentage of each type of assessment and the final midterm mark

# PLAN(PSEUDOCODE):
# 0. Define constants
#    - the minimum and maximum grade
#    - weight of each assessment type
#    - assessment names
#    - number of activities
# 1. Calculate the weight of in class activities, assignment 1 and the 1 test, sum will equal to 0.44
# 2. Figure out equation for weight
#    - Midterm mark = (Mark * Weight)/sum of weights
#    - Midterm mark = (grade1 * 0.05 + grade2 * 0.05 + grade3 * 0.05 + grade4 * 0.05 + assignment * 0.08 + test * 0.16) / 0.44
# 3. Ask user input based on the three categories for grade calculation
#    - Ask user for all 4 class activity grades
#    - Ask user for Assignment 1 grade
#    - Ask user for Test 1 grade
# 4. I will have to make sure user inputs are validated to account for user error
#    - Valid input will be determined as a whole number between 0 and 100
#    - .isdigit() will make sure the input is only numeric digits
# 5. I will make use of lists to store user entries
#    - One list for assessment names that wont change, and one for the grades,
# 6. Using lists, group the grades by the three different categories
# 7. Calculate the midterm mark in code form using the formula from step 2
# 8. Allow the program to pause so the user can look at the results and press enter to exit

# PROGRAM:
# Constants: 
MIN_GRADE = 0
MAX_GRADE = 100
CLASS_ACTIVITY_WEIGHT = 0.05
NUMBER_OF_ACTIVITIES = 4
ASSIGNMENT_WEIGHT = 0.08
TEST_WEIGHT = 0.16
TOTAL_WEIGHT = NUMBER_OF_ACTIVITIES * CLASS_ACTIVITY_WEIGHT + ASSIGNMENT_WEIGHT + TEST_WEIGHT
ASSESSMENT_NAMES = ("Planning Activity", "Numeric Activity", "Selection Activity", "Iteration Activity", "Assignment 1", "Test 1")

grades = list()

# Ask for each grade until its valid
for name in ASSESSMENT_NAMES:
    is_valid = False

    while is_valid != True:
        grade_input = input(f"Please enter your grade for {name}: ")
        if grade_input.isdigit():
            grade = int(grade_input)
            if grade >= MIN_GRADE and grade <= MAX_GRADE:
                grades.append(grade)
                is_valid = True
            else:
                print(f"Invalid input: Please enter a number between {MIN_GRADE} and {MAX_GRADE}.")
        else:
            print("Invalid input: Please enter a whole number.")

# Group the grades by the three categories asked in the problem
class_activities_total = 0
for count in range(0, NUMBER_OF_ACTIVITIES):
    class_activities_total += grades[count]

class_activities_percentage = class_activities_total / NUMBER_OF_ACTIVITIES
assignment_percentage = grades[4]
test_percentage = grades[5]

# Weighted midterm mark in equation form
midterm_mark = (class_activities_total * CLASS_ACTIVITY_WEIGHT + grades[4] * ASSIGNMENT_WEIGHT + grades[5] * TEST_WEIGHT) / TOTAL_WEIGHT

# Final output
print()
print(f"Class activities: {class_activities_percentage:.2f}%")
print(f"Assignment 1: {assignment_percentage:.2f}%")
print(f"Test 1: {test_percentage:.2f}%")
print(f"Midterm mark: {midterm_mark:.2f}%")

input("Press Enter to exit program")

# DESKCHECK:
# If I enter chicken on the first input:
# - I get: Invalid input: Please enter a whole number.

# If I enter a number outside the range of 0 and 100 
# - I get: Invalid input: Please enter a number between 0 and 100.

# If I enter a negative or any decimal number I get: 
# - Invalid input: Please enter a whole number.

# If I input all 100 on all asked inputs I should get 100% on everything
# - I get:
# Class activities: 100.00%
# Assignment 1: 100.00%
# Test 1: 100.00%
# Midterm mark: 100.00%
# Press Enter to exit program

# Final check: If I input 0 on all class activities but input 100 on assignment 1 and test 1 I get 54.55%, verification:
# 0(grade) * 0.20(combined weight of all 4 activities) = 0 points
# 100(grade) * 0.08(weight) = 8
# 100(grade) * 0.16(weight) = 16
# 0+8+16 = 24 divided by total weight of 0.44 we get: 54.55%