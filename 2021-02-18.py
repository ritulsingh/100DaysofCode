# Topics Covered -> Control flow: if else, while loop, for loop, break and continue

# Control flow: if else
# Example 1:
age = int(input("Enter your age: "))
if age > 18:
    print("You can Vote!")
else:
    print("You can not Vote!")

# Example 2:
a,b = [int(i) for i in input("Enter the number: ").split()]
if a > b:
    print("a grater than b")
elif a == b:
    print("a and b are equal")
else:
    print("b grater than a")

# Control flow: while loop
# The while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
    # print(i)
    i += 1 

# Control flow: break and continue
# The break statement we can stop the loop even if the while condition is true
# Example 1:
i = 1
while i < 9:
    # print(i)
    if i == 5:
        break
    i += 1

# Example 2:
# the continue statement we can stop the current iteration, and continue with the next
i = 0
while i < 9:
    i += 1
    if i == 5:
        continue
    # print(i)

# Control flow: for loop
# Example 1:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Example 2:
for x in "banana":
  print(x)

# Example 3:
for x in range(6):
  print(x)

# Example 4
# The range() function defaults to 0 as a starting value,however it is possible
# to specify the starting value by adding a parameter: range(2, 6)
for x in range(2, 6):
  print(x)

# Example 5:
for x in range(0,10,2):
  print(x)