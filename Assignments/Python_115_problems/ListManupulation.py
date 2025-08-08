# 28. List Manipulation: Given a list of integers, write a Python program using a for loop to find the sum, average, maximum, and minimum values in the list.

aList = [1,2,50,3,500,4,10,100]
lenList = len(aList)
sum = avg = maximum = 0
for i in aList:
    sum+=i
    if i > maximum:
        maximum = i
    else:
        maximum = maximum
minimum = aList[0]
for j in aList:
    if i < minimum:
        minimum = i
    else:
        minimum = minimum
avg = sum/lenList
print(f"sum = {sum}, average = {avg}, maximum = {maximum}, minimum = {minimum}")



