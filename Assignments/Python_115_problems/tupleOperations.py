# 56. Tuple Operations: Given two tuples of integers, write a Python program to perform element-wise addition, subtraction, and multiplication and create new tuples for each operation.

a = (1,2,3,4,5,6)
b = (6,5,4,3,2,1)

addittion = list()
subtraction = list()
multiplication = list()

for i in range(len(a)):
    addittion.append(a[i]+b[i])
    subtraction.append(b[i]-a[i])
    multiplication.append(a[i]*b[i])
print(tuple(addittion))
print(tuple(subtraction))
print(tuple(multiplication))






