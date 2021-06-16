#coding:utf-8

"""
list, dictonary comprehension
-------------------------------"""


# list classic way
list_1 = []
for i in range(10):
	list_1.append(i**2) # to the power of 2

# list comprehension
list_2 = [i**2 for i in range(10)]

# nested list
list_3 = [[i**2 for i in range(10)] for j in range(3)]


# dictionary classic way
dict_1 = {
	'0': 'Jean',
	'1': 'Pierre',
	'2': 'Marc'
}

# dictionary comprehension (enumerate)
names = ['Jean', 'Pierre', 'Marc']
dict_2 = {key:value for key, value in enumerate(names)}

# dictionary comprehension (zip)
ages = [10, 20, 30]
dict_3 = {name:age for name, age in zip(names, ages)}

# dictionary comprehension (enumarate) with condition
dict_4 = {name:age for name, age in zip(names, ages) if age >=20}

# tuple comprehension
tuple_1 = tuple((i**2 for i in range(10)))


print(list_1)
print(list_2)
print(list_3)
print(dict_1)
print(dict_2)
print(dict_3)
print(dict_4)
print(tuple_1)



# ex chap 5 : sort positive and negative numbers in a dictionnary
print('\nex chap 5:\n-----------------------')

filing_cabinet = {
	'positive': [],
	'negative': []
}

def sort(filing_cabinet, nbr):
	if nbr >= 0:
		filing_cabinet['positive'].append(nbr)
	else:
		filing_cabinet['negative'].append(nbr)

	return filing_cabinet

# test
sort(filing_cabinet, -2)
sort(filing_cabinet, 3)
sort(filing_cabinet, 6)
print(filing_cabinet)

# ex chap 6 : create dictionary, keys (0->20), values(key to the power of 2)
print('\nex chap 6:\n-----------------------')

nbrs = [i**2 for i in range(21)]
dict_power = {k:v for k, v in enumerate(nbrs)}
print(dict_power)

