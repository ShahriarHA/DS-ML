# 84. Dictionary Frequency Count: Write a Python program that takes a string as input and creates a dictionary containing each character as a key and its frequency as the value.



t = input("Enter a string: ")


freq_dict = {}


for c in t:
    freq_dict[c] = freq_dict.get(c, 0) + 1


print("Character Frequency Dictionary:", freq_dict)









