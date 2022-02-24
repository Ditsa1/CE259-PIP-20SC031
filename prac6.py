# 20CS031 - DITSA MANDANI
# Repo. Link - https://github.com/Ditsa1/CE259-PIP-20SC031

lst = []

for i in range(int(input())):
    str1 = input()
    lst.append(str1)
   
freq = {}

for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
        
val = list(freq.values())
for i in val:
    print(i, end = ' ')