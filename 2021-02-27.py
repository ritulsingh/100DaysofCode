# Topics Covered-> Space and Time Complexity: Find largest number in a list , Binary search, Find elements common in two lists,
# Find elements common in two lists using a Hashtable/Dict

# Find largest number in a list
lst = []
n = int(input("Enter a number: "))
largest = 0
for i in range(n):
    exe = int(input())
    if exe > largest:
        largest = exe
    lst.append(exe)
print("Largest number in list is {}".format(largest)) # time complexity O(n)

# Binary search Time Complexity O(log n)
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
arr = [ 2, 3, 4, 10, 40 ]
x = 10
result = binary_search(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

# Find elements common in two lists O(n)
lst1 = [65,84,58,69,14]
lst2 = [15,24,58,79,84]
element = []
for i in range(0, len(lst1)):
    for j in range(0, len(lst2)):
        if lst1[i] == lst2[j-1]:
            element.append(lst1[i])
print("The common elements in list 1 and list 2: ", element)


# Find elements common in two lists using a Hashtable/Dict
from collections import Counter 
def commonElement(ar1,ar2,ar3): 
	ar1 = Counter(ar1) 
	ar2 = Counter(ar2) 
	ar3 = Counter(ar3) 
	resultDict = dict(ar1.items() & ar2.items() & ar3.items()) 
	common = [] 
	for (key,val) in resultDict.items(): 
		for i in range(0,val): 
			common.append(key) 

	print(common) 
if __name__ == "__main__": 
	ar1 = [1, 5, 10, 20, 40, 80] 
	ar2 = [6, 7, 20, 80, 100] 
	ar3 = [3, 4, 15, 20, 30, 70, 80, 120] 
	commonElement(ar1,ar2,ar3) 
