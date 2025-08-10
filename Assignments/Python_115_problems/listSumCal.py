# 105. List Sum Calculator: Write a Python function called `list_sum` that takes a list of integers as input and returns the sum of all elements in the list. Test the function with different lists.

def list_sum(a):
    # pass
    sum = 0
    for i in a:
        sum+=i
    return sum

aList = list(map(int,input().split()))
p = list_sum(aList)


print(p)


