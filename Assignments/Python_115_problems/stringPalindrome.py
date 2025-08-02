# String Palindrome: Write a Python function to check if a given string is a palindrome or not.
# "madam, "racecar, "level, "pop, and "12321"


def stringPalindorme(d):
    reversedD = d[::-1]
    if d == reversedD:
        print("Given string is a palindrome")
    else:
        print("Given string is not a palindrome")

a = str(input())
stringPalindorme(a)
# print(reverse_a)
# if a == reverse_a:
#     print("yes! string is a palindrome")
# else:
#     print("not! string is not a palindrome")

