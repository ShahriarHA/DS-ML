# 14. Grades Classification: Write a Python program that takes a student’s percentage as input and prints their corresponding grade according to the following criteria: – 90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail

StudentPercentage = int(input())
if StudentPercentage >= 90:
    print("Grade: A+")
elif StudentPercentage >= 80 and StudentPercentage <= 89:
    print("Grade: A")
elif StudentPercentage >= 70 and StudentPercentage <= 79:
    print("Grade: B")
elif StudentPercentage >= 60 and StudentPercentage <= 69:
    print("Grade: C")
elif StudentPercentage < 60:
    print("Fail!")
    


