# Made by: Guillaume Amorim
# November/12/2026
# Class: Intro to programming, COSC1100
# In class activity: Functions

# PROBLEM: Turn previous class activity into functions

# PLAN(PSEUDOCODE):
# Changing the class activity(arrays) for mid term grades into functions where possible.
# I will seperate the code into functions:
# - Newly added defined function to get a valid grade
# - Defined a function to get all the grades
# - Defined a function to calculate the weighted midterm mark
# - Defined a function to display results
# For the section where the program will run I added:
# - Defined start() function to show where the program starts
# I decided to write out all 4 activity grades instead of using a loop.
# Finally, I call start() at the bottom of the file to run the program.

# PROGRAM SECTION: 
# Constants: 
MIN_GRADE = 0
MAX_GRADE = 100
CLASS_ACTIVITY_WEIGHT = 0.05
NUMBER_OF_ACTIVITIES = 4
ASSIGNMENT_WEIGHT = 0.08
TEST_WEIGHT = 0.16
TOTAL_WEIGHT = NUMBER_OF_ACTIVITIES * CLASS_ACTIVITY_WEIGHT + ASSIGNMENT_WEIGHT + TEST_WEIGHT
ASSESSMENT_NAMES = ("Planning Activity", "Numeric Activity", "Selection Activity", "Iteration Activity", "Assignment 1", "Test 1")

# Newly added defined function to get a valid grade
def get_valid_grade(name):
    is_valid = False

    while is_valid != True:
        grade_input = input(f"Please enter your grade for {name}: ")
        if grade_input.isdigit():
            grade = int(grade_input)
            if grade >= MIN_GRADE and grade <= MAX_GRADE:
                is_valid = True
            else:
                print(f"Invalid input: Please enter a number between {MIN_GRADE} and {MAX_GRADE}.")
        else:
            print("Invalid input: Please enter a whole number.")
            
    return grade

# Defined a function to get all the grades
def get_all_grades():
    grades = list()
    for name in ASSESSMENT_NAMES:
        grades.append(get_valid_grade(name))
    return grades

# Defined a function to calculate the weighted midterm mark
def calculate_midterm_mark(class_activities_total, assignment_grade, test_grade):
    return (class_activities_total * CLASS_ACTIVITY_WEIGHT
            + assignment_grade * ASSIGNMENT_WEIGHT
            + test_grade * TEST_WEIGHT) / TOTAL_WEIGHT

# Defined a function to return the final results
def display_results(class_activities_percentage, assignment_percentage, test_percentage, midterm_mark):
    print()
    print(f"Class activities: {class_activities_percentage:.2f}%")
    print(f"Assignment 1: {assignment_percentage:.2f}%")
    print(f"Test 1: {test_percentage:.2f}%")
    print(f"Midterm mark: {midterm_mark:.2f}%")

    input("Press Enter to exit program")

# This is where the program starts.
# For the purpose of clarity I decided to write out all 4 activity grades instead of using a loop.
def start():
    grades = get_all_grades()

    class_activities_total = grades[0] + grades[1] + grades[2] + grades[3]
    class_activities_percentage = class_activities_total / NUMBER_OF_ACTIVITIES
    assignment_percentage = grades[4] # Refers to Assignment 1
    test_percentage = grades[5] # Refers to Test 1

    midterm_mark = calculate_midterm_mark(class_activities_total, assignment_percentage, test_percentage)

    display_results(class_activities_percentage, assignment_percentage, test_percentage, midterm_mark)

start()
