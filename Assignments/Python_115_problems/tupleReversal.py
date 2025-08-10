# 54. Tuple Reversal: Write a Python program to reverse a tuple without using any built-in functions.
a = (1,2,3,4,5,6)
# print(len(a))
b = list()
for i in range(len(a)-1,-1,-1):
    # print(a[i])
    b.append(a[i])
# print(b)
b_tuple = tuple(b)
print(b_tuple,type(b_tuple))
