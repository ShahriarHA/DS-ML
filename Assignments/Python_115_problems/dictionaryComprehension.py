# 85. Dictionary Comprehension: Given a list of integers, write a Python program to create a dictionary where the keys are the elements from the list, and the values are their squares.


aList = [1,2,3,4]
aDict = {}

for i in aList:
    aDict[i] = i**2
print(aDict)

