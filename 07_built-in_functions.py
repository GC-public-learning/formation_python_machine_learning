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

# format
print('x = {}'.format(x))

# format new version
print(f'x = {x}')

# handle files

# open a file with such name (file created if it doesn't exist)
# w -> write, r -> read, a -> write on the end (add), other modes exist... 
f = open('my_file.txt', 'w')

# write in a file
f.write('Hello World !')

# close the file
f.close()

# open a file to read
f = open('my_file.txt', 'r')

# read the file
print(f.read())
f.close()

# conventional way ("close()"" isn't needed with "with" operator)
with open('my_file.txt', 'w') as f:
	# write numbers (0->9) with their power of 2 on severals different lines
	for i in range(10):
		f.write(f'{i} to the power of 2 = {i**2}\n')
		
"""
exercice
----------------"""

# make in a list with each line of the last created file
print('\nex with readline()\n------------------------')
with open('my_file.txt', 'r') as f:
	# write numbers (0->9) with their power of 2 on severals different lines
	list_1 = f.readlines()
	print(list_1)

# remove the carriage return (\n) with regular expressions
print('\nex with readline() and remove the carriage return with regex\n'
	'-----------------------------------------------------------------')

import re

with open('my_file.txt', 'r') as f:
	# write numbers (0->9) with their power of 2 on severals different lines
	list_1 = []

	for l in f.readlines():
		# re.sub() -> replace "matched" by a "string" in such "string"
		list_1.append(re.sub('\\n$','',l)) 
	
print(list_1)


# remove the carriage return (\n) with regular expressions
print('\nex with read() and remove the carriage return with regex\n'
	'-----------------------------------------------------------------')

with open('my_file.txt', 'r') as f:
	list_1 = []
	for line in re.findall('.*\\n', f.read()):
		list_1.append(re.sub('\\n$','',line))
	print(list_1)
