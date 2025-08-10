# 111. Factorial Calculation: Write a recursive Python function called `factorial` that takes a non-negative integer as input and returns its factorial.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a integer: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {n} is {factorial(n)}")


