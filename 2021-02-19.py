# Topics Covered -> Lists, Tuples, Sets
# Lists:->
# Lists are used to store multiple items in a single variable. Lists are created using square brackets.
lst = ["ram", "ritul", "singh"]
print(lst)

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# Allow Duplicates -> Since lists are indexed, lists can have items with the same value
thisList = ["apple", "banana", "cherry", "apple", "cherry"]
print(thisList)

# type() From Python's perspective, lists are defined as objects with the data type 'list':
print(type(thisList))

# The list() Constructor -> It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Tuples:->
# Tuples are used to store multiple items in a single variable and it is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
thisTuple = ("ram", "ritul", "singh")
print(thisTuple)

# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


# One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# A tuple can contain different data types.
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

myTuple = ("apple", "banana", "cherry")
print(type(myTuple))

# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Sets:->
# Sets are used to store multiple items in a single variable.
# A set is a collection which is both unordered and unindexed.
# Sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Set items are unordered, unchangeable, and do not allow duplicate values.
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.

# Sets cannot have two items with the same value. Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

set1 = {"abc", 34, True, 40, "male"}
print(set1)

# It is also possible to use the set() constructor to make a set.
# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)