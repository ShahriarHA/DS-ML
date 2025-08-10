# 40. List Manipulation: Given two lists of integers, write a Python program to create a new list that contains elements common to both lists.

a = [10,30,20,60]
b = [10,50,20,40]

commonList = []

for i in a:
    for j in b:
        if j == i:
            commonList.append(i)
print(commonList)


