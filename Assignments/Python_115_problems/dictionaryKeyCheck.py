# 86. Dictionary Key Check: Write a Python program that takes a key as input and checks if it exists in a given dictionary. Print “Key Found” if the key is present and “Key Not Found” otherwise.
itemPrice = {
    "apple": 100,
    "cherry":90,
    "banana": 80,
    "mango": 110
}

dictKey = str(input())
for x,y in itemPrice.items():
    if dictKey == x:
        print("Found")
    else:
        print("key not found")



