# 92. Prime Number Checker: Write a Python program that takes a number as input and determines if it is a prime number or not. Use a `for` loop to check for factors. If a factor is found, `break` out of the loop.

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num}")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
