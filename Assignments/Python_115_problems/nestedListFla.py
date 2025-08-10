# 60. Nested List Flattening: Write a Python program to flatten a nested list and convert it into a single-dimensional list.
a = [[1,2,3,4],[23,45]]

flatten_a = []
for i in a:
    if type(i) is type(a):
        flatten_a.extend(i)
    else:
        flatten_a.append(i)
print(flatten_a)