# Number Pyramid: Write a Python program using nested loops to print a number pyramid like the following: 1 22 333 4444 55555

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    
    for k in range(1, 2*i):
        print(i, end="")
    print()


