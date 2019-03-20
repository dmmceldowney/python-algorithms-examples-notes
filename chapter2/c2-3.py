# Big-O notation

# Self Check

# Write two Python functions to find the minimum number in a list. 

#The first function should compare each number to every other number on the list O(n**2). 

#The second function should be linear O(n).
# build list
"""
# random list
import random
list = [7, 3, 1, 6, 6, 8, 10, 4, 4, 1, 6]
for i in range (0, 11):
    list.append(random.randrange(1, 11))
print(list)
"""
# static list
list = [7, 3, 1, 6, 6, 8, 10, 4, 4, 1, 6]


# Compare each number to every other number on the list [O(n**2)]
smallest = -1
for item1 in list: # n
    if smallest == -1:
        smallest = item1
    # compare it to every other item in the list
    for item2 in list: # n
        if item1 < item2 and item1 <= smallest:
            smallest = item1

print(smallest)


# Linear Dude [O(n)]
smallest = -1
for item in list: # n
    if smallest == -1  or smallest > item:
        smallest = item 
print(smallest)
