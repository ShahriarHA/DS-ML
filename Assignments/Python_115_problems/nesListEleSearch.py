# 68. Nested List Element Search: Write a Python program to search for a specific element in a nested list and return its position (row and column indices).
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]


searchItem = 8
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == searchItem:
            print(f"element is found in {i}'th row and {j}'th column")
        else:
            pass
