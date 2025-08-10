# 107. Leap Year Checker: Write a Python function called `is_leap_year` that takes a year as input and returns `True` if it is a leap year and `False` otherwise. Test the function with different years.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

years = [2000, 2004, 1900, 2023, 2024]
for y in years:
    print(f"{y}: {is_leap_year(y)}")


