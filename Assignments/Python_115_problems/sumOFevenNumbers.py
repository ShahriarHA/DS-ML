# 25. Sum of Even Numbers: Write a Python program using a while loop to calculate the sum of all even numbers between 1 and N, where N is taken as input from the user.

n = int(input())

sum = 0
i = 1
while i <= n:
    if i%2 == 0:
        sum+=i
    i+=1
print(sum)

