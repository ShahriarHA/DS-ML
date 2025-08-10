# 100. Vowel Counter: Write a Python program that takes a string as input and counts the number of vowels (a, e, i, o, u) in it. Use a `for` loop and `continue` to skip counting non-vowel characters.


word = str(input("enter a word: "))
count = 0

for i in word.lower():
    if i == 'a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
    else:
        continue
print(count)
