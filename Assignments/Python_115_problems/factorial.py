# 102. Factorial Calculator: Write a Python function called `factorial` that takes an integer as input and returns its factorial. Test the function with different values.

def factorial(n):
    # pass
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        mul = 1
        for i in range(n,0,-1):
            mul*=i
        return mul

n = int(input("enter a number: "))
fact = factorial(n)
print(fact)
