# 51. Tuple Sorting: Write a Python program to sort a tuple of integers in ascending order.
a = (3,1,5,4,9,8,7,2,1)
b = list(a)
# print(b)
b.sort()
# print(b)
c = tuple(b)
print(c,type(c))