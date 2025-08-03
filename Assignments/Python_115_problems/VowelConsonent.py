# 15. Vowel or Consonant: Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.

char = str(input())

if ((char == "A" or char == "a") or (char == "E" or char == "e") or (char == "i" or char == "I") or (char == "o" or char == "O") or (char == "U" or char == "u")):
    print("Vowel!")
else:
    print("Consonant!")


