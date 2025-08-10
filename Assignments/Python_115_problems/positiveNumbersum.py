# 96. Positive Number Sum: Write a Python program that takes positive numbers as input until a negative number is entered. Then, calculate and print the sum of all positive numbers entered. Use a `while` loop and `break` to exit the loop when a negative number is encountered.

sum = 0
while True:
    n = int(input("enter a number: "))
    if n >= 0:
        sum+=n
    else:
        break
print(f"sum of all positive numbers {sum}")

