# 82. Dictionary Key Removal: Given a dictionary of items and their quantities, write a Python program to remove a specific item from the dictionary based on user input.


itemPrice = {
    "apple": 100,
    "cherry":90,
    "banana": 80,
    "mango": 110
}

userInput = str(input())
itemPrice.pop(userInput)
print(itemPrice)


