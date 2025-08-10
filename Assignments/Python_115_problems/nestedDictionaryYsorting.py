# 90. Nested Dictionary Sorting: Given a nested dictionary containing product details (product name, price, and quantity), write a Python program to sort the products based on their prices in ascending order.
products = {
    "P001": {"name": "Laptop", "price": 75000, "quantity": 5},
    "P002": {"name": "Smartphone", "price": 35000, "quantity": 10},
    "P003": {"name": "Headphones", "price": 2000, "quantity": 50},
    "P004": {"name": "Monitor", "price": 15000, "quantity": 7}
}
sorted_products = dict(sorted(products.items(), key=lambda x: x[1]["price"]))
print(sorted_products)