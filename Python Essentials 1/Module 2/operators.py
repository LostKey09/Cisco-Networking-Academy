###########################################
# Operators
# Author: Aldrine Drebb L. Cristobal
# Date: June 2024
###########################################

# Exponentiation
print(2 ** 3) # 2 raised to the power of 3
print(2. ** 3) # 2.0 raised to the power of 3
print(2 ** 3.) # 2 raised to the power of 3.0
print(2. ** 3.) # 2.0 raised to the power of 3.0

# Multiplication
print(2 * 3) # 2 multiplied by 3
print(2. * 3) # 2.0 multiplied by 3
print(2 * 3.) # 2 multiplied by 3.0
print(2. * 3.) # 2.0 multiplied by 3.0

# Division
print(6 / 3) # 6 divided by 3
print(6. / 3) # 6.0 divided by 3
print(6 / 3.) # 6 divided by 3.0
print(6. / 3.) # 6.0 divided by 3.0

# Integer/float division
print(6 // 4) # 6 integer divided by 4
print(6. // 4) # 6.0 integer divided by 4
print(-6 // 4) # -6 integer divided by 4
print(6. // -4) # 6.0 integer divided by -4

# Modulo
print(14 % 4.) # Remainder of 14 divided by 4
print(14 % 4.5) # Remainder of 14 divided by 4.5

# Addition
print(2 + 3) # 2 plus 3
print(2. + -3.) # 2.0 plus -3.0

# Subtraction
print(-4 - 4) # -4 minus 4
print(-4. - 4) # -4.0 minus 4
print(-1.1) # Unary minus operator applied to 1.1
print(+(-1.1)) # Unary plus operator applied to -1.1, which does not change the value

# Priority of operators
print(2 + 3 * 4) # Multiplication has higher precedence than addition
print(9 % 6 % 2) # Modulo is left-sided, so it is evaluated from left to right
print(2 ** 3 ** 2) # Exponentiation is right-sided, so it is evaluated from right to left
# ** | + - (unary)| * / // % | + - (from highest to lowest precedence)

# Parentheses
print((2 + 3) * 4) # Parentheses change the order of evaluation
