# 76. Set Membership Test: Write a Python program that takes an element as input and checks if it exists in a given set. Print “Found” if the element is present and “Not Found” otherwise.

a = {1,2,3,4,5,6,7,8,9,10}
n = int(input())
# if n in a:
#     print("Found")
# else:
#     print("Not Found")

print("Found") if n in a else print("Not Found")

