# 88. Nested Dictionary Length: Write a Python program to calculate and print the total number of key-value pairs in a nested dictionary.

students = {
    "student1": {
        "name": "Shahriar",
        "age": 20,
        "address": "Dhaka, Bangladesh"
    },
    "student2": {
        "name": "Hussain",
        "age": 19,
        "address": "Sylhet, Bangladesh"
    }
}

for x,y in students.items():
    print(f"total number of key-value pairs in {x} are {len(y)}")


