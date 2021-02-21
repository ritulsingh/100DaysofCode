# Topics Covered-> Types of functions, Function arguments, Recursive functions, Lambda functions, Modules, Packages, File Handling, Exception Handling
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# Creating a function:->
def MyFunction():
    return "Hello World"

# Calling a Function
print(MyFunction())

# Function Argument:-> Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
def MyFunction(name):
    return name + " Singh"
print(MyFunction("Ritul"))
print(MyFunction("Ram"))

# Parameters or Arguments :-> The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called

# Number of Argument:-> By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less
def MyFunction(fname, lname):
    return fname + " " + lname
print(MyFunction("Ritul", "Singh"))
print(MyFunction("Ram", "Singh"))

# Arbitrary Arguments, *args:-> If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def MyFunction(*kids):
  print("The youngest child is " + kids[1])
MyFunction("Emil", "Tobias", "Linus")

# Keyword Arguments:-> You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs:-> If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Ritul", lname = "Singh")

# Default Parameter Value:-> The following example shows how to use a default parameter value. If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument:-> You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Return Values:-> To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement:-> function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass

# Recursion:-> Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)

# Lambda functions:-> A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax:-> lambda arguments : expression
x = lambda a: a + 10
print(x(5))

# Lambda functions can take any number of arguments:
x = lambda a, b: a + b + 10
print(x(5,10))
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Why Use Lambda Functions?;:-> The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n
myDoubler = myfunc(2)
print(myDoubler(11))  

# File Handling:-> File handling is an important part of any web application. Python has several functions for creating, reading, updating, and deleting files.
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
f = open("demofile.txt")
f = open("demofile.txt", "rt")
print(f.read())
print(f.readline())
f.close()

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

# Delete a File:-> To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.remove("demofile.txt")

# Check if file exists, then delete it:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

# Exception Handling:->
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
try:
  print(x)
except:
  print("An exception occurred")

# Many Exceptions:-> You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
# Print one message if the try block raises a NameError and another for other errors:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# You can use the else keyword to define a block of code to be executed if no errors were raised:
# In this example, the try block does not generate any error:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Raise an exception:-> As a Python developer you can choose to throw an exception if a condition occurs. To throw (or raise) an exception, use the raise keyword.
# Raise an error and stop the program if x is lower than 0:
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

# The raise keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user.
# Raise a TypeError if x is not an integer:
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
