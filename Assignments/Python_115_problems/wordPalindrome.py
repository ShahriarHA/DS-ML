# 97. Word Palindrome Checker: Write a Python program that takes a word as input and checks if it is a palindrome (reads the same forwards and backward). Use `continue` to skip checking the word if its length is less than 3 characters.


while True:
    word = str(input("enter a word: "))
    if len(word) < 3:
        continue
    else:
        if word == word[::-1]:
            print("it is palindrome")
            break
        else:
            print("not palindrome")
            



