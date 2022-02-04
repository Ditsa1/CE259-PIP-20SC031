# 20CS031 - DITSA MANDANI
# Repo. Link - https://github.com/Ditsa1/CE259-PIP-20SC031

# size of family
k = int(input())

# room number of each family member
rooms = (int(x) for x in input().split(' '))
seen = {}

# frequency of each room number
for i in rooms:
    if not i in seen:
        seen[i] = 1
    else:
        seen[i] += 1

# printing room number which has frequency 1 (captain's room)
for key, val in seen.items():
    if val != k:
        print(key)