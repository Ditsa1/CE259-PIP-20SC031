# 20CS031 - DITSA MANDANI
# Repo. Link - https://github.com/Ditsa1/CE259-PIP-20SC031

# take n words
for i in range(int(input())):

    str1 = input()
    n = len(str1)

    # divide string into left half and right half
    if n%2 == 0:
        l, r = str1[:n//2], str1[n//2:]
    else:
        l, r = str1[:n//2], str1[n//2+1:]

    # sort the left and right sides and see if they match
    # string is lapindrome if they match
    if sorted(l) == sorted(r):
        print("YES")
    else:
        print("NO")