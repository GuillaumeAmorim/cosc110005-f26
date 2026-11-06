# Made by: Guillaume Amorim
# 11/3/2026
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
# Pre-Class Activities and Class Exercises combined = whole number 0-100
# Assignment 1 = whole number 0-100
# Test 1 = whole number 0-100

# OUTPUTS: 
# Output will be the final calculated mid term grade and percentage for the type of of assessment.

# PLAN(PSEUDOCODE):
# 0. Calculate the weight of in class activities, assignment 1 and the 1 test, sum will equal to 0.44
# 1. Figure out equation for weight
#    - Midterm mark = (Mark * Weight)/sum of weights
#    - Midterm mark = (class_grade * 0.2 + assignment_grade * 0.08 + test_grade * 0.16) / 0.44
# 2. Ask user input based on the three categories for grade calculation
#    - Ask user for all Pre-Class Activities and Class Excercises grades as one combined grade
#    - Ask user for Assignment 1 grade
#    - Ask user for Test 1 grade
# 3. I will have to make sure user inputs are validated to account for user error
#    - Valid input will be determined as a whole number between 0 and 100
# 4. I will make use of lists to store user entries

# PROGRAM:
# Constants: 
# MIN_GRADE = 0
# MAX_GRADE = 100
# CLASS_ACTIVITIES = 0.20
# ASSIGNMENT1 = 0.08
# TEST1 = 0.16

grades = []

user_input = False

