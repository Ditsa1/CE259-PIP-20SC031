# 20CS031 - DITSA MANDANI
# Repo. Link - https://github.com/Ditsa1/CE259-PIP-20SC031

# creating an empty list
list1 = []

# number of elements in list
n = int(input())

# iterating till the range
for i in range(0, n): 
    entry = int(input())    
    list1.append(entry) # adding the element

# sorting list in reverse oder
list1.sort(reverse=True)

# finding second largest number
for i in range(0,n):
    if list1[i] != list1[i+1]:
        ans = list1[i+1]
        break

print("Answer:", ans)
        
    




