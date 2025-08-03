# 8. Quadratic Equation Solver: Write a Python program that takes the coefficients (a, b, c) of a quadratic equation as input and calculates and prints the real roots (if they exist) or a message indicating the complex roots.
import cmath
a = int(input())
b = int(input())
c = int(input())

d = (b**2) - (4*a*c)

res1 = (-b + cmath.sqrt(d)) / (2*a)
res2 = (-b - cmath.sqrt(d)) / (2*a)

print(res1,res2)


