###########################################
# Literals
# Author: Aldrine Drebb L. Cristobal
# Date: June 2024
###########################################

# Integers
print(11111111)
print(11_111_111)
print(-11_111_111)
print(0b10101010) # Binary
print(0o12345670) # Octal
print(0x12345678) # Hexadecimal

# Floating-point numbers
print(4.0)
print(4E1) # Exponential notation
print(4E-1) # Exponential notation with negative exponent
print(0.0000000000000000000001) # Printing by exponential notation 

# Strings
# I like "Monty Python".
print("I like \"Monty Python\".")
print('I like "Monty Python".')
# I'm Monty Python.
print("I'm Monty Python.")
print('I\'m Monty Python.')

# Booleans
print(True > False)
print(True < False)

#################LAB#################
# Expected output:
#"I'm"
#""learning""
#"""Python"""
print("\"I\'m","\"learning\"", "\"\"Python\"\"", sep="\"\n\"", end="\"\n")