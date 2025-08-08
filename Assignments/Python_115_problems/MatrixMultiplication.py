# 32. Matrix Multiplication: Write a Python program using nested loops to multiply two matrices.

a = [[1,2,4],
     [2,3,4],
     [4,5,6]]
b = [[10,8,4],
     [5,4,3],
     [1,2,4]]

# print(a[2][2])

for i in range(0,3):
    for j in range(0,3):
        sum = 0
        for k in range(0,3):
            sum+=a[i][k]*b[k][j]
        print(sum, end=" ")
    print()




