# 81. Dictionary Merging: Given two dictionaries, write a Python program to merge them into a single dictionary and print the result.

itemPrice = {
    "apple": 100,
    "cherry":90,
    "banana": 80,
    "mango": 110
}
StudentDict = {
    "Shahriar": 100,
    "Hussain":90,
    "Arif": 80,
    "Daizi": 100
}

mergedItems = itemPrice|StudentDict
print(mergedItems)


