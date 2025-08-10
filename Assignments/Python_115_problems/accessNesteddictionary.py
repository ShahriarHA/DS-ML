# 87. Access Nested Dictionary: Given a nested dictionary containing student details, write a Python program to access and print specific information such as a student’s name, age, and address.


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

print(students["student2"]["name"])

print(students["student1"]["address"])


