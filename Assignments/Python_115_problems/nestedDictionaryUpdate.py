# 89. Nested Dictionary Update: Given a nested dictionary of employee details, write a Python program to update an employee’s salary based on their employee ID.


employees = {
    "E001": {
        "name": "Alice",
        "position": "Software Engineer",
        "salary": 50000
    },
    "E002": {
        "name": "Bob",
        "position": "Data Analyst",
        "salary": 45000
    }
}
newSalary = 40000
employee_ID = "E001"

for x,y in employees.items():
    if x == employee_ID:
        y["salary"] = newSalary
    else:
        pass
print(employees)
