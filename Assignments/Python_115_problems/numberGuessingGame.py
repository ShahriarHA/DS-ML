# 99. Number Guessing Game: Write a Python program that generates a random number between 1 and 100 and lets the user guess the number. Use a `while` loop, `break` when the correct number is guessed, and `continue` to keep prompting the user until they guess correctly.z

import random

while True:
    n = random.randint(1,100)
    print(n)
    userN = int(input("enter any number between 1 to 100: "))

    if n == userN:
        print("you won!")
        break
    else:
        continue


