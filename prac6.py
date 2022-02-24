# 20CS031 - DITSA MANDANI
# Repo. Link - https://github.com/Ditsa1/CE259-PIP-20SC031

lst = []

# take n words from user and add to a list
for i in range(int(input())):
    str1 = input()
    lst.append(str1)

# create empty dictionary 
freq = {}

# add element from list as key and its freq as value in dictionary
for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# convert list to set to remove repeated elements and print number of distinct elements
set1 = set(lst)
print(len(set1))

# print freq of elements in list       
val = list(freq.values())
for i in val:
    print(i, end = ' ')