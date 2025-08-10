# 101. Unique Characters: Write a Python program that takes a string as input and checks if it contains all unique characters (no character repeats). Use a `for` loop and `break` when a character repeats.
word = str(input())

cout = 0
for i in word:
    # print(word.count(i))
    if word.count(i) >= 2:
        print("word repeated!")
        break
    else:
        continue
    

