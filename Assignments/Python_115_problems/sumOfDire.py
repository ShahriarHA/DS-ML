# 113. The sum of Digits: Write a recursive Python function called `sum_of_digits` that takes an integer as input and returns the sum of its digits.
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

num = int(input("Enter a number: "))
print(f"Sum of digits of {num} is {sum_of_digits(num)}")
