# Topics Covered-> Numpy Introduction, Numerical operations on Numpy
# NumPy Array Iterating:-> Iterating means going through elements one by one. As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python
# Iterate on the elements of the following 1-D array
import numpy as np
arr = np.array([1,2,3])
for x in arr:
    print(x)

# Iterate on the elements of the following 2-D array
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x) #If we iterate on a n-D array it will go through n-1th dimension one by one.

# Iterate on each scalar element of the 2-D array
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    for y in x:
        print(y)

# Iterate on the elements of the following 3-D array
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    print(x)

# Iterate on each scalar element of the 3-D array
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

# Iterating Arrays Using nditer()
# The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration, lets go through it with examples.
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)

# Iterating Array With Different Data Types
# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

# Iterate through every scalar element of the 2D array skipping 1 element:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)

# Enumerated Iteration Using ndenumerate()
# Enumeration means mentioning sequence number of somethings one by one.
# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.
# Enumerate on following 1D arrays elements:
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

# Enumerate on following 2D array's elements:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

# Joining NumPy Arrays:-> Joining means putting contents of two or more arrays in a single array.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

# Join two 2-D arrays along rows (axis=1):
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

# Joining Arrays Using Stack Functions
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

# Splitting NumPy Arrays
# Split the array in 3 parts:
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

# Split the array in 4 parts:
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)

# Access the splitted arrays:
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])

# Split the 2-D array into three 2-D arrays.
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

# Split the 2-D array into three 2-D arrays.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)

# Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)

# NumPy Searching Arrays
# Find the indexes where the value is 4:
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
# The example above will return a tuple: (array([3, 5, 6],)

# Find the indexes where the values are even:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

# The searchsorted() method is assumed to be used on sorted arrays.
# Find the indexes where the value 7 should be inserted:
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

# Search From the Right Side
# By default the left most index is returned, but we can give side='right' to return the right most index instead.
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

# Find the indexes where the values 2, 4, and 6 should be inserted:
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

# Sort the array:
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

# Sort the array alphabetically:
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

# Sort a boolean array:
arr = np.array([True, False, True])
print(np.sort(arr))

# Sort a 2-D array:
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

# NumPy Filter Array
# Create an array from the elements on index 0 and 2:
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)
# The example above will return [41, 43], why?
# Because the new filter contains only the values where the filter array had the value True, in this case, index 0 and 2.

# Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43, 44])
# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# Random Numbers in NumPy
# Generate a random integer from 0 to 100:
from numpy import random
x = random.randint(100)
print(x)

# Generate a random float from 0 to 1:
x = random.rand()
print(x)

# Generate a 1-D array containing 5 random integers from 0 to 100:
x=random.randint(100, size=(5))
print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
x = random.randint(100, size=(3, 5))
print(x)

# The rand() method also allows you to specify the shape of the array.
# Generate a 1-D array containing 5 random floats:
x = random.rand(5)
print(x)

# Return one of the values in an array:
x = random.choice([3, 5, 7, 9])
print(x)

# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

# NumPy ufuncs:-> ufuncs stands for "Universal Functions" and they are NumPy functions that operates on the ndarray object.
# Without ufunc, we can use Python's built-in zip() method:
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
  z.append(i + j)
print(z)

# NumPy has a ufunc for this, called add(x, y) that will produce the same result.
# With ufunc, we can use the add() function:
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z)
