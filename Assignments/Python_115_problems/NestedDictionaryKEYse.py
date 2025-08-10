# 91. Nested Dictionary Key Search: Write a Python program that takes a key as input and searches for it in a nested dictionary. If found, print the corresponding value, otherwise, print “Key Not Found.”

products = {
    "P001": {"name": "Laptop", "price": 75000, "quantity": 5},
    "P002": {"name": "Smartphone", "price": 35000, "quantity": 10},
    "P003": {"name": "Headphones", "price": 2000, "quantity": 50},
    "P004": {"name": "Monitor", "price": 15000, "quantity": 7}
}


inputKEY = str(input())
for j in products.values():
    for i,k in j.items():
        # print(i)
        if i == inputKEY:
            print(k)
        else:
            print("Key Not Found")





