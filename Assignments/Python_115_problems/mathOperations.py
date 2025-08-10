# 108. Math Operations: Write a Python function called `math_operations` that takes three numbers and a string representing an operation (‘add’, ‘subtract’, ‘multiply’, or ‘divide’). The function should return the result of the specified operation on the three numbers. Implement the math operations as nested functions.

def math_operations(a,b,c,ch):
    # pass
    if ch == "+":
        return (a+b+c)
    elif ch == "-":
        return (a-b-c)
    elif ch == "/":
        return ((a/b)/c)
    else:
        return (a*b*c)

a = int(input("enter a = "))
b = int(input("enter b = "))
c = int(input("enter c = "))
ch = str(input("enter ch = "))

p = math_operations(a,b,c,ch)
print(p)





