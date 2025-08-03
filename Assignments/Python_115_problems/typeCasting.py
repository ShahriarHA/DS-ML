# 10. Typecasting Challenge: Given three variables: `a = ‘100’`, `b = 25`, and `c = ‘10.5’`, write a Python program to perform the following operations and print the results: – Convert `a` to an integer and add it to `b`. – Convert `c` to a float and subtract it from the result of the first operation. – Convert the final result to a string and concatenate it with the string ” is the answer.”

a, b, c = "100",25, "10.5"
# print(a,b,c)
add = int(a)+b
print(add)
substruct = add - float(c)
print(substruct)
print(f"{str(substruct)} is the answer")

