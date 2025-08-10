# 48. List of Lists Concatenation: Given a list of nested lists, write a Python program to concatenate all the sublists into a single flat list.

# list concatenation using extend and append method


a = [10,[1,2,3,4],33,34,[23,45]]

flatten_a = []
for i in a:
    if type(i) is type(a):
        flatten_a.extend(i)
    else:
        flatten_a.append(i)
print(flatten_a)


