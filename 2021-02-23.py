# Topics Covered-> Numpy Introduction, Numerical operations on Numpy
# NumPy is a python library used for working with arrays.
# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
# Installation of NumPy-> pip install numpy
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

# Check NumPy version
print(np.__version__)

# Check the type of the object
print(type(arr))

# Use tuple to create a NumPy array
arr = np.array((1,2,3,4,5))
print(arr)

# Dimensions in Arrays
# 0-D Arrays :-> 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
arr = np.array(12)
print(arr)

# 1-D Arrays:-> An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
arr = np.array([1,5,7,8,9])
print(arr)

# 2-D Arrays:-> An array that has 1-D arrays as its elements is called a 2-D array. These are often used to represent matrix or 2nd order tensors.
arr = np.array(([5,2,6],[2,8,9]))
print(arr)

# 3-D Arrays:-> An array that has 2-D arrays (matrices) as its elements is called 3-D array. These are often used to represent a 3rd order tensor.
arr = np.array([[2,5,6],[1,2,3],[4,8,6]])
print(arr)

# Check number of dimensions
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher Dimensional Arrays
# An array can have any number of dimensions. When the array is created, you can define the number of dimensions by using the ndmin argument.
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
# In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.

# Access 1-D Array Elements
arr = np.array([1,5,6,7,8])
print(arr[0])

# get the second element of array
print(arr[1])

# Get third and fourth elements from the following array and add them.
print(arr[2] + arr[3])

# Access 2-D Array Elements
arr = np.array([[1,5,6,5,4],[5,6,2,3,5]])
print("2ncd element on 1st dim: ",arr[0, 1])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd dim: ', arr[1, 4])

# Access 3-D Array Elements
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

# Negative Indexing-> Use negative indexing to access an array from the end.
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

# Numpy Array Slicing
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# Slice elements from index 4 to the end of the array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

# Slice elements from the beginning to index 4 (not included):
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

# Negative Slicing
# Slice from the index 3 from the end to index 1 from the end:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

# Use the step value to determine the step of the slicing:
# Return every other element from index 1 to index 5:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

# Return every other element from the entire array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])

# Slicing 2-D array
# From the second element, slice elements from index 1 to index 4 (not included):
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

# From both elements, return index 2:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])

# Data Types in NumPy
# NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.
# Below is a list of all data types in NumPy and the characters used to represent them.
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

# Checking the Data Type of an Array
# The NumPy array object has a property called dtype that returns the data type of the array:
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# Get the data type of an array containing strings:
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

# Create an array with data type string:
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)
# For i, u, f, S and U we can define size as well.

# Create an array with data type 4 bytes integer:
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

# Converting Data Type on Existing Arrays
# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
# Change data type from float to integer by using 'i' as parameter value:
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

# Change data type from float to integer by using int as parameter value:
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

# Change data type from integer to boolean:
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

# NumPy Array Copy vs View
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array
# Copy:-> Make a copy, change the original array, and display both arrays
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

# View:-> Make a view, change the original array, and display both arrays
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

# Make a view, change the view, and display both arrays
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)

# Check if Array Owns it's Data
# Print the value of the base attribute to check if an array owns it's data or not.
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)

# Shape of an array
# Print the shape of a 2-D array:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
# The example above returns (2, 4), which means that the array has 2 dimensions, and each dimension has 4 elements.

# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

# What does the shape tuple represent?
# Integers at every index tells about the number of elements the corresponding dimension has.
# In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.

# Reshaping arrays:-> Reshaping means changing the shape of an array
# Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

# Convert the following 1-D array with 12 elements into a 3-D array.
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

# Check if the returned array is a copy or a view:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)

# Convert 1D array with 8 elements to 3D array with 2x2 elements:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)
# Note: We can not pass -1 to more than one dimension.

# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this. Convert the array into a 1D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)