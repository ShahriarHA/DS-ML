# 65. Count Even Numbers: Write a Python program to count the number of even numbers in a nested list.
a = [[10,2,3,4,5],[8,7,6,5,4,3,3]]

for sublist in a:
    count = 0
    for i in sublist:
        if i%2 == 0:
            count+=1
        else:
            count = count
    print(f"total even numbers in {sublist} are {count}")





