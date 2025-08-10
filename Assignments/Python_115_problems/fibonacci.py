def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

N = int(input())
if N < 0:
    print("Fibonacci is not defined for negative numbers.")
else:
    print(f"The {N}th Fibonacci number is {Fibonacci(N)}")
