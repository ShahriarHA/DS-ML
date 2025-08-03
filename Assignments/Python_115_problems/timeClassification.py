# 16. Time Classification: Write a Python program that takes the time in hours (24-hour format) as input and prints “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.

TimeInHoure = int(input())

if TimeInHoure >= 5 and TimeInHoure < 12:
    print("Good Morning")
elif TimeInHoure >= 12 and TimeInHoure < 17:
    print("Good Afternoon")
elif TimeInHoure >= 17 and TimeInHoure < 21:
    print("Good evening")
else:
    print("Good Night")

