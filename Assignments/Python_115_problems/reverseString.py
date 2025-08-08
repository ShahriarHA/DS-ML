# 29. Reverse String: Write a Python program using a while loop to reverse a given string.
aSTRING = str(input())
revString = ""
i = len(aSTRING)-1
# print(i)
while i >= 0:
    # print(aSTRING[i])
    revString = revString+aSTRING[i]
    i-=1
print(revString)
