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
# Pre-Class Activities and Class Excercises = 20% or 0.2
# -Planning an Application = 5% weight or 0.05
# -Numeric and String Data = 5% weight or 0.05
# -Selection = 5% weight or 0.05
# -Iteration = 5% weight or 0.05
# Test 1 = 16% weight or 0.16

# PLAN(PSEUDOCODE):
# 0. Calculate the weight of all 4 in class activities and the 1 test
# 1. Figure out equation for weight
#    - Midterm mark = (Mark * Weight)/sum of weights
#    - Midterm mark = (Grade1 * 0.05 + Grade2 * 0.05 + Grade3 * 0.05 + Grade4 * 0.05 + Grade5 * 0.16) / 0.36 
# 2. Ask user input for grade calculation
#    - Ask for all Pre-Class_Activities and Class Excercises grades as one combined grade
#    - Ask for Test 1 grade
# 3. I will have to make sure inputs are validated to account for user error
#    - Valid input will be determined as a whole number between 0 and 100 and is an integer
# 4.

# OUTPUTS: 
# Output will be the final calculated mid term grade and percentage for the type of of assessment.