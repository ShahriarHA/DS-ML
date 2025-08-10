# 66. Maximum Element in Nested List: Write a Python program to find the maximum element in a nested list of integers.
a = [[10,2,3,4,5],[8,7,6,100,5,4,3,3]]

for sublist in a:
    print(f"the maximum element of {sublist} is {max(sublist)}")
