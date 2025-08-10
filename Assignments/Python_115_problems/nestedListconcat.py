# 64. Nested List Concatenation: Given a list of nested lists, write a Python program to concatenate all the sublists into a single flat list.

a = [[1,2,3],[3,4,5]]
flatList = []
for sublist in a:
    flatList.extend(sublist)

print(flatList)


