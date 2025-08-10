# 83. Dictionary Sorting: Given a dictionary with names as keys and corresponding ages as values, write a Python program to sort the dictionary based on age in ascending order.

StudentDict = {
    "Shahriar": 20,
    "Hussain": 19,
    "Arif": 35,
    "Daizi": 30
}

sorted_students = dict(sorted(StudentDict.items(), key=lambda item: item[1]))

print("Original dictionary:", StudentDict)
print("Sorted dictionary by age:", sorted_students)






