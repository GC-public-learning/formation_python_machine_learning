#coding:utf-8

"""
built-in functions
-------------------------------"""

"""
all built-in functions are listed on internet 
"""

x = -3.14159
numbers = [i for i in range(10)]
booleans = [True, False, True]

# absolute value
print(abs(x))

# round x digits after comma
print(round(x, 1))

# max of a list
print(max(numbers))

# min of a list
print(min(numbers))

# length of a list
print(len(numbers))

# sum of numbers of a list
print(sum(numbers))

# and logical operation of a list
print(all(booleans))

# or logical operation of a list
print(any(booleans))

# type
print(type(x))

# convert in string (possible int, float, etc...)
print(type(str(x)))

# possible to convert list in tuple or dict and vice versa
print(tuple(numbers))

# convert in a binary number (possible exa, bit etc...)
print(bin(127))

# record keyboard entries (return a string)
input("enter a string: ")