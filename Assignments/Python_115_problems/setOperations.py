# 74. Set Operations: Given three sets A, B, and C, write a Python program to find and print the intersection of A and B, the union of B and C, and the difference between C and A

a = {2,4,7,8}
b = {3,9,7,5}
c = {10,20,30}

intesection = a.intersection(b)
print(f"Intersection: {intesection}")

union = b.union(c)
print(f"Union : {union}")

diff = c.difference(a)
print(f"difference: {diff}")



