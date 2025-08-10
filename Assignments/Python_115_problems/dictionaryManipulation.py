
# 77. Dictionary Manipulation: Given a dictionary with student names as keys and their corresponding scores as values, write a Python program to add a new student to the dictionary and update the score of an existing student.

StudentDict = {
    "Shahriar": 100,
    "Hussain":90,
    "Arif": 80
}
# add a new student
StudentDict['Daizi'] = 100
print(StudentDict)

# update the score of an existing student.
StudentDict["Hussain"] = 80
print(StudentDict)


