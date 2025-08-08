# 27. Prime Number Checker: Write a Python program using a while loop to check if a given number N is prime or not.

n = int(input())

if n > 1:
    if n == 2:
        print("it is a prime number")
    else:
        factors = []
        if n%1 == 0 and n%n == 0:
            i = 2
            while i < n:
                if n%i == 0:
                    factors.append(i)
                i+=1
            print(factors)
            if len(factors) == 0:
                print("it is a prime number")
            else:
                print("it is not a prime number")
            
        



