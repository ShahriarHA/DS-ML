# 17. Triangle Type Checker: Write a Python program that takes three sides of a triangle as input and determines whether it forms an equilateral, isosceles, or scalene triangle.

side1 = int(input())
side2 = int(input())
side3 = int(input())

if side1 == side2 == side3:
    print("equilateral")
elif (side3 == side2) or (side2 == side1) or (side1 == side3):
    print("isosceles")
else:
    print("scalene")

