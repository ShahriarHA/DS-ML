# 45. Flatten Nested List: Write a Python program to flatten a given nested list and convert it into a single-dimensional list.

a = [10,[1,2,3,4],33,34,[23,45]]
# print(f"{a}")
# print(type(a[1]),type(a))
flatten_a = []
for i in a:
    if type(i) is type(a):
        flatten_a.extend(i)
    else:
        flatten_a.append(i)
print(flatten_a)




