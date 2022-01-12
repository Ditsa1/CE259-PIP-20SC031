# 20CS031 - DITSA MANDANI
# Repo. Link - 
# Dictionary
# a. Write a Python script to check whether a given key already exists in a dictionary.
# b. Write a Python script to merge two Python dictionaries.
# c. Write a Python program to sum all the items in a dictionary.
# d. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
# e. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print('Dictionary:')
print('--------------------------\n') 

dic1 = {'a':1, 'b':2, 'c':3, 'd':4}
key = 'b'
if key in dic1:
    print('Given key exists.')
else:
    print('Given key does not exist.')

print('--------------------------\n') 
dic2 = {'e':5, 'f':6, 'g':7, 'h':8}

dic1.update(dic2)
print(dic1)
print('--------------------------\n') 
print('Sum: ', sum(dic1.values()))
print('--------------------------\n') 
dic1['i'] = 9
print(dic1)
print('--------------------------\n') 
dic3 = {0:10, 1:20}
dic3[2] = 30
print(dic3)
print('--------------------------\n') 
dic4 = {1:10, 2:20}
dic5 = {3:30, 4:40}
dic6 = {5:50, 6:60}

dic7 = {}
dic7.update(dic4)
dic7.update(dic5)
dic7.update(dic6)

print(dic7)

print('--------------------------\n') 

# Tuple
# a. Write a Python program to create a tuple with different data types.
# b. Write a Python program to create a tuple with numbers and print one item.
# c. Write a Python program to add an item in a tuple.
# d. Write a Python program to convert a tuple to a string.
# e. Write a Python program to find the length of a tuple.

print('Tuple:')
print('--------------------------\n') 

tup1 = (1, 'a', 5.9, 'hello')
print(tup1)

print('--------------------------\n') 
tup2 = (1, 2, 3, 4, 5, 6, 7)
print(tup2[4])
print('--------------------------\n') 
tup2 = list(tup2)
tup2.append(8)
tup2 = tuple(tup2)
print(tup2)

print('--------------------------\n') 

tup3 = ('h', 'e', 'l', 'l', 'o')
str = ''.join(tup3)
print(str)
print('--------------------------\n') 
print(len(tup2))
print('--------------------------\n') 

# Set
# a. Write a Python program to add member(s) in a set and clear a set
# b. Write a Python program to remove an item from a set if it is present in the set.
# c. Write a Python program to create an intersection, Union, difference of sets.
# d. Write a Python program to find maximum and the minimum value in a set.
# e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

print('Set:')
print('--------------------------\n') 

set1 = {'one', 'two', 'three', 'four', 'five'}
set1.add('six')
print(set1)
set1.clear()
print(set1)

print('--------------------------\n') 

set1 = {'one', 'two', 'three', 'four', 'five'}
if 'two' in set1:
    set1.remove('two')

if 'six' in set1:
    set1.remove('one')
print(set1)

print('--------------------------\n') 

set2 = {1, 2, 3, 4, 5, 6, 7, 8}
set3 = {2, 4, 6, 8}

print(set2.intersection(set3))
print(set2.union(set3))
print(set2.difference(set3))

print('--------------------------\n') 

print(max(set2))
print(min(set2))

print('--------------------------\n') 

lista = [2, 1, 4, 2, 2, 5, 5, 6, 6, 7, 7, 7, 7, 2, 0, 1, 3, 2, 2, 2]
tupa = (3, 4, 5, 7, 8, 2, 3, 4, 4, 3, 4, 4, 5, 6, 6, 6, 4, 4, 4)
dicta = {0:1, 1:2, 2:3, 3:3, 4:1, 5:1, 5:3, 6:1, 7:2, 8:1}

temp = list(dicta.values())

print('Most common element:', max(set(lista), key = lista.count), 'Count:', lista.count(max(set(lista), key = lista.count)))
print('Most common element:', max(set(tupa), key = tupa.count), 'Count:', tupa.count(max(set(tupa), key = tupa.count)))
print('Most common element:', max(set(dicta), key = temp.count), 'Count:', temp.count(max(set(dicta), key = temp.count)))


