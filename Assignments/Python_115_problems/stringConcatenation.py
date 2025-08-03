# 9. String Concatenation: Write a Python program that takes two strings as input and concatenates them into a single string without using the `+` operator.

string1 = str(input())
string2 = str(input())

# concatenation using f string
print(f"{string1} {string2}")

# concatenation using join method
l = [string1, string2]
print(" ".join(l))



