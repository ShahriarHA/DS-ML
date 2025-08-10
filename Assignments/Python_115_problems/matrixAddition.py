# 44. Matrix Addition: Write a Python program to add two matrices represented as nested lists.
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
b = [[1,3,5],
     [2,4,6],
     [3,5,7]]

# c = a+b
c = list()
# print(a)

# print(len(a))
for i in range(0,len(a)):
    sumList = []
    for j in range(0,len(b)):
        sum = 0
        sum = a[i][j] + b[i][j]
        # print(sum,end=" ")
        sumList.append(sum)
    c.append(sumList)
    # print()
    # print(sumList)
print(c)

