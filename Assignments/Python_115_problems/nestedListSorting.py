# 61. Nested List Sorting: Given a nested list containing lists of integers, write a Python program to sort the sublists based on their lengths.

a = [[1,2],[2,3,4,5,6,7,8],[2,3,4]]
# a.sort()
print(a)
sorted_A = sorted(a,key=len)
print(sorted_A)



