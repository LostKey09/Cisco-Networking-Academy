##########################################
# Variables
# Author: Aldrine Drebb L. Cristobal
# Date: June 2024
##########################################

# Variable naming
# uppercase letters, lowercase letters, digits, and underscores
# cannot start with a digit
# case-sensitive
# cannot be a reserved keyword
name = "Python"
print(name)

# Shortcut operators
x = 1
x = x * 2
print(x)
x *= 2
print(x)
sheep = 1
sheep = sheep + 1
sheep += 1
print(sheep)
# +=, /=, %=, -=, **=

#################LAB#################
# create the variables: john, mary, and adam;
# assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
# having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
# now create a new variable named total_apples equal to the addition of the three previous variables.
# print the value stored in total_apples to the console;
# experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations on them (e.g., +, -, *, /, //, etc.). Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples.
john = 3
mary = 5
adam = 6
print("Apples: John has", john, "and Mary has", mary, "and Adam has", adam)
total_apples = john + mary + adam
print("Total Number of Apples:", total_apples)
# Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts:
# miles to kilometers;
# kilometers to miles.
kilometers = 12.25
miles = 7.38
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
# Take a look at the code in the editor: it reads a float value, puts it into a variable named x, and prints the value of a variable named y. Your task is to complete the code in order to evaluate the following expression:
# 3x3 - 2x2 + 3x - 1
# The result should be assigned to y.
# Remember that classical algebraic notation likes to omit the multiplication operator ‒ you need to use it explicitly. Note how we change data type to make sure that x is of type float.
x = -1
x = float(x)
y = 3*(x ** 3) - 2*(x ** 2) + 3*(x) -1
print("y =", y)