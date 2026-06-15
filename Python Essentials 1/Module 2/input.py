##########################################
# Variables
# Author: Aldrine Drebb L. Cristobal
# Date: June 2024
##########################################

# Sample Input()
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

# # Input()'s output is string
# anything = input("Enter a number: ")
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# Typecasting
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# String operators
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("\nWelcome, " + fnam +" "+ lnam + ".") # Concatenation

print((fnam+" ") * 3) # Repetition

# Type conversion
print(str(123*2/3))

#################LAB#################
# Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.
# The results have to be printed to the console.
# You may not be able to protect the code from a user who wants to divide by zero. That's okay, don't worry about it for now.
# input a float value for variable a here
a = float(input("First number: "))
# input a float value for variable b here
b = float(input("Second number: "))
# output the result of addition here
print("Addition:", str(a+b))
# output the result of subtraction here
print("Subtraction:", str(a-b))
# output the result of multiplication here
print("Multiplication:", str(a*b))
# output the result of division here
print("Division:", str(a/b))
print("\nThat's all, folks!")

# Your task is to complete the code in order to evaluate the following expression: 1/x+1/x+1/x+1/x
x = float(input("Enter value for x: "))
y = 1/(x+1/(x+1/(x+(1/x))))
print("y =", y)

# Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes 
# (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). 
# The result has to be printed to the console.
# For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
print((str((hour+((mins+dura)//60))%24) if (mins+dura>=60) else str(hour))+ ":"+ (str((mins+dura)%60) if (mins+dura>=60) else str(mins+dura)))