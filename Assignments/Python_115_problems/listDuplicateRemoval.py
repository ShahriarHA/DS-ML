# 42. List Duplicates Removal: Write a Python program to remove duplicates from a given list while preserving the order of the elements.

a = [20,20,30,30,30,40,20,50,60]
duplicateValue = list()

for i in a:
    if i not in duplicateValue:
        duplicateValue.append(i)
            
print(duplicateValue)



