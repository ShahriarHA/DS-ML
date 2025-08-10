# 46. List Element Frequency: Given a nested list containing lists of integers, write a Python program to count the frequency of each element in the entire nested list.
a = [10,[1,2,3,4],10,34,[1,2]]
flatten_a = []
for i in a:
    if type(i) is type(a):
        flatten_a.extend(i)
    else:
        flatten_a.append(i)
print(flatten_a)
# print(flatten_a.count(10))
for i in flatten_a:
    print(f"the frequency of {i} is {flatten_a.count(i)}")
