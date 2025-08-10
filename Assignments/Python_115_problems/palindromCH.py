# 103. Palindrome Checker: Write a Python function called `is_palindrome` that takes a string as input and returns `True` if it is a palindrome and `False` otherwise. Test the function with different words.

def is_palindrome(s):
    # pass
    if s == s[::-1]:
        return True
    else:
        return False

word = str(input())
p = is_palindrome(word)
print(p)