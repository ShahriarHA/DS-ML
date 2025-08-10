# 47. Transpose Matrix: Write a Python program to transpose a given matrix represented as a nested list.
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

transposd = []
print(f"before transpose: {a}")
for i in range(0,len(a)):
    newRow = []
    for j in range(0,len(a)):
        newRow.append(a[j][i])
    transposd.append(newRow)
print(f"after transpose: {transposd}")
                   