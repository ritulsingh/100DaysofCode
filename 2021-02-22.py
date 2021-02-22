# Topics Covered-> Debugging Python
# Debugging Python code using breakpoint() and pdb
# Let’s see some basics of debugging using built-in function breakpoint() and pdb module.
# Syntax:
# 1-> breakpoint()           # in Python 3.7 
# 2-> import pdb; pdb.set_trace()   # in Python 3.6 and below
# Method 1: Using breakpoint() function
def fun(a,b):
    breakpoint()
    result = a / b
    return result
print(fun(5, 0))

# Commands for debugging :
# c -> continue execution
# q -> quit the debugger/execution
# n -> step to next line within the same function
# s -> step to next line in this function or a called function

# Method 2 : Using pdb module
def fun(a,b):
    import pdb; pdb.set_trace()
    result = a / b
    return result
print(fun(5, 0))

def debugger(a): 
    import pdb; pdb.set_trace() 
    result = [a[element] for element in range(0, len(a)+5)] 
    return result 
print(debugger([1, 2, 3]))