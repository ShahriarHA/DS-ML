# 39. List Reversal: Write a Python program to reverse a given list without using any built-in functions.

a = [10,20,30,40,11,22,33,55,44]
# print(a[0:])
# print(a[:-1])
revList = []
for i in range(len(a)-1,-1,-1):
    revList.append(a[i])
print(revList)




