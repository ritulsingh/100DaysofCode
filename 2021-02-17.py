# Topics Covered -> Keywords and identifiers, comments, indentation and statements, Variables and data types in Python, Standard Input and Output, Operators.

# Examples of valid identifiers:
# var1
# _var1
# _1_var
# var_1

# Examples of invalid identifiers
# !var1
# 1var
# 1_var
# var#1

# Keywords
print(True and True)
print(True or False)
print(not True)

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

x = 5
print(type(x))

# Setting the Specific Data Type
x = int(20)
print(type(x))

# Input in python
n = int(input("Enter a number: "))

# Output
print("The number is :",n)

# Input or Output
username = input("Enter username:")
print("Username is: " + username)
