# 31. Print Patterns: Write a Python program using nested loops to print the following pattern:

n = int(input())

for i in range(0,n):
    for j in range(0,i+1):
        print("*", end="")
    print()