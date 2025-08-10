# 80. Dictionary Value Search: Given a dictionary of items and their prices, write a Python program to search for an item based on its price and print the item’s name.
StudentDict = {
    "apple": 100,
    "cherry":90,
    "banana": 80,
    "mango": 110
}

itemPrice = 80
for x,y in StudentDict.items():
    if y == itemPrice:
        print(f"the item name is '{x}'")