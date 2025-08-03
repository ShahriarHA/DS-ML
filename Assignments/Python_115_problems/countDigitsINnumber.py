# 23. Count Digits in a Number: Write a Python program using a while loop to count the number of digits in a given integer N.
n = int(input())
str_n = str(n)
lenOfN = len(str_n)
i = 0
count = 0
while i < lenOfN:
    count+=1
    i+=1
print(f"{count} digits")
