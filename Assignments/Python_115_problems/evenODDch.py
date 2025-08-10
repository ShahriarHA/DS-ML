# 104. Even or Odd Checker: Write a Python function called `even_or_odd` that takes an integer as input and returns “Even” if the number is even and “Odd” if the number is odd. Test the function with different numbers.

def even_or_odd(n):
    # pass
    if n%2 == 0:
        return "Even"
    else:
        return "odd"
n = int(input())
p = even_or_odd(n)
print(p)

