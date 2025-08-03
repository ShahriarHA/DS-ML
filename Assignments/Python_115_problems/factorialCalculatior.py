# 21. Factorial Calculator: Write a Python program using a while loop to calculate the factorial of a given number N.
num = int(input())
if num == 0:
    print(1)
elif num == 1:
    print(1)
else:
    fact = num
    while(num != 1):
        fact = fact*(num-1)
        # print(fact)
        num-=1
    print(fact)