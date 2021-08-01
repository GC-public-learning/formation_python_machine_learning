#coding:utf-8

"""
numpy
-------------------------------"""

# ndarray (n dimensions array)

import numpy as np

# init an array filled with such numbers
a1 = np.array([1,2,3])
print(a1)

# shape (number of rows for each dimension) -> tuple
print(a1.shape)

# number of elements
print(a1.size)

# make an array filled with zeros with such shape
a2 = np.zeros((3, 2))
print(a2)

# make an array filled with "1" with such shape
a3 = np.ones((3,2))
print(a3)

# make an array filled withsuch number with such shape
a4 = np.full((2, 3), 9)
print(a4)

# make an array filled with random number (normal distribution centered in zeros
a5 = np.random.randn(3,4)
print(a5)

# fix the random numbers (always the sames)
num = 1
np.random.seed(num)

# make an array filled with such number (1) to such number(2) and shuch number of steps (3)
print(np.linspace(0, 10, 20))

# make an array 1 dimnension with indices 0 -> 10 are filled with such step
print(np.arange(0, 10, 1))

# dtype specify the type for the numbers -> int, float etc...
print(np.linspace(0, 10, 20, dtype=np.float64))

# -------------------------------------------------------------

"""
handle arrays
----------------"""
a1 = np.ones((2, 3))
a2 = np.zeros((2, 3))

# merge 2 arrays vertically
a3 = np.hstack((a1, a2))
print(a3)

# merge 2 arrays horizontally
a4 = np.vstack((a1, a2))
print(a4)

# merge 2 arrays with such axe
a5 = np.concatenate((a1, a2), axis=0) # same than vstack
print(a5)

# reshape array (carefull to keep the same size)
a6 = a5.reshape(12,)
print(a6)

# make a better tuple result with shape() function for array with one dimension
# -> nomraly return (n,)
# -> needed (n, 1)
print(a6.shape)
a6 = a6.reshape(a6.shape[0], 1)
print(a6.shape)

# return with the default shape (needed to for some operations graphics, img, etc...)
a6 = a6.squeeze() # remove all dimensions with value 1
print(a6.shape)

# ravel() -> flatten an array in one dimension
print (np.ones((2, 3)).ravel())



