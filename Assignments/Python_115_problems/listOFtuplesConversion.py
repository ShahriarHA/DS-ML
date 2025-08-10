# 62. List of Tuples Conversion: Given a nested list containing tuples of (x, y) coordinates, write a Python program to convert it into a list of x-coordinates and a list of y-coordinates.

a = [[(1, 2), (3, 4)], [(5, 6)], [(7, 8), (9, 10)]]
x_cooor = []
y_coor = []

for sublist in a:
    # print(sublist)
    for x,y in sublist:
        x_cooor.append(x)
        y_coor.append(y)
print(x_cooor)
print(y_coor)

# c,d = ["h","O"]
# print(c,d)
