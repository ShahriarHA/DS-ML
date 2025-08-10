# 106. Greatest Common Divisor (GCD) Calculator: Write a Python function called `gcd` that takes two integers as input and returns their greatest common divisor. Test the function with different pairs of numbers.

def gcd(a1,a2):
    # pass
    gcd_l = []
    for i in range(2,a2):
        if (a1%i == 0) and (a2%i == 0):
            gcd_l.append(i)
    return max(gcd_l)

num1 = int(input())
num2 = int(input())

p = gcd(num1,num2)
print(p)
