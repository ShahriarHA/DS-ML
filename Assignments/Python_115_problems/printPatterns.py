# 26. Print Patterns: Write a Python program using nested for loops to print various patterns, such as a right-angled triangle, an inverted right-angled triangle, and so on.


n = int(input())

# right-angled triangle
for i in range(0,n):
    for j in range(0,i+1):
        print("#", end="")
    print()



# inverted right-angled triangle
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()

# left angle triangle
for i in range(0,n):
    for j in range(0,n-(i+1)):
        print(" ",end="")
    for k in range(0,i+1):
        print("@",end="")
    print()

# inverted left angle triangle
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(" ", end='')
    for k in range(0,i):
        print("$", end="")
    print()





