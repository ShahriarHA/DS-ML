# 67. Diagonal Sum of Matrix: Given a square matrix represented as a nested list, write a Python program to calculate the sum of the elements in the main diagonal.

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
sumOfdiagonalElements = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if i == j:
            sumOfdiagonalElements += a[i][j]
print(sumOfdiagonalElements)





