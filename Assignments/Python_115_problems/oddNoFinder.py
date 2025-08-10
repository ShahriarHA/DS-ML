# 98. Odd Number Finder: Write a Python program to find the first odd number from a list of integers. Use a `for` loop and `break` to stop the loop when the first odd number is found.

a = [0,2,3,4,5,6,7]
for i in a:
    if i%2 == 1:
        print(f"{i} is first odd number")
        break
    else:
        pass
    

