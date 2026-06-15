##########################################
# Functions
# Author: Aldrine Drebb L. Cristobal
# Date: June 2024
##########################################

print("The itsy bitsy spider climbed up the waterspout.")
print("Down came the rain and washed the spider out.")

# Spacing with empty print() function
print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")

# Newline character \n
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")

# Multiple arguments
print("The itsy bitsy spider", "climbed up", "the waterspout.")

# Positional arguments
print("My name is", "Python.")
print("Monty Python.")

# Keyword arguments
print("My name is", "Python.", end=" ")
print("Monty Python.")

# Multiple keyword arguments
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

#################LAB#################
# Expected output: Programming***Essentials***in...Python
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")
# Minimize the number of print() function invocations by inserting the \n sequence into the strings
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n")
# Duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring"
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n" * 2)