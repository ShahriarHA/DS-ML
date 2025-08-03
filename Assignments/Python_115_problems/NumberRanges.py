# 19. Number Ranges: Write a Python program that takes an integer as input and prints whether the number falls within the ranges: 0-50, 51-100, 101-150, or above 150.

num = int(input())

if num >= 0 and num <= 50:
    print(f"{num} falls within 0-50 range")
elif num >= 51 and num <= 100:
    print(f"{num} falls within 51-100 range")
elif num >= 101 and num <= 150:
    print(f"{num} falls within 101-150 range")
else:
    print(f"{num} is above 150")



