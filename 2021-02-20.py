# Topics Covered -> Dictionary, Strings, Data Structures
# Dictionary:->
# Dictionaries are used to store data values in key: value pairs.
# A dictionary is a collection which is ordered, changeable and does not allow duplicates.
distTest = {
    'name':"ritul",
    'lastName':"Singh",
    'dob':"16/10/2001"
}
print(distTest)
print(distTest["name"]) # we can access the value by key

# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# To determine how many items a dictionary has, use the len() function.
print(len(thisdict))

# The values in dictionary items can be of any data type, String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

# Print the data type of a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

# To determine if a specified key is present in a dictionary use the in keyword:
# Example
# Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Print all key names in the dictionary, one by one using for loop
for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])

# You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)

# String:->
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello". You can display a string literal with the print() function:
print("Hello World")
print('Hello World')

# You can assign a multiline string to a variable by using three quotes:
# Example
# You can use three double quotes:
a = """Hello,
World."""
print(a)
# Or three single quotes:
a = '''Hello,
World.'''
print(a)

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
a = "Hello, World!"
print(a[1])

# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Example
# Loop through the letters in the word "HelloWorld":
for x in "HelloWorld":
  print(x)

# To get the length of a string, use the len() function.
# Example
# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

# To check if a certain phrase or character is present in a string, we can use the keyword in.
# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

# Slicing-> You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5])

# Slice From Start
print(b[:5])

# Slice from the end
print(b[5:])

# Negative Indexing -> Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])

# Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)