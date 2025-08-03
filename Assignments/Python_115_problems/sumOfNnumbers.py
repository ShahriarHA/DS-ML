# 20. Sum of N Numbers: Write a Python program using a for loop to calculate the sum of the first N natural numbers, where N is taken as input from the user.

n = int(input())
sum = 0
for i in range(0,n):
    # print(i)
    sum += i
print(sum)

