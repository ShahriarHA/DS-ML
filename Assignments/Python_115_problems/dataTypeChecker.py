# 6. Data Type Checker: Write a Python function that takes a variable as input and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).

def DataTypeChecker(data):
    # pass

    if type(data) is list:
        return "List"
    elif type(data) is int:
        return "int"
    elif type(data) is str:
        return "str"
    elif type(data) is float:
        return "float"

# for integer
int_a = int(input())
dataType = DataTypeChecker(int_a)
print(dataType)

# for float
float_b = float(input())
dataType_b = DataTypeChecker(float_b)
print(dataType_b)

# for a list
l = []
dataType_l = DataTypeChecker(l)
print(dataType_l)

