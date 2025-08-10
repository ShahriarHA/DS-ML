# 110. Temperature Converter: Write a Python function called `temperature_converter` that takes a temperature value and a string representing the scale (‘C’ for Celsius or ‘F’ for Fahrenheit) as input. The function should convert the temperature from one scale to the other using nested functions and return the converted value.
# (50°F − 32) × 5/9 
# (0°C × 9/5) + 32 

def Fahrenheit(a):
    print(a*(9/5)+32)
def celcius(a):
    print((a - 32)*(5/9))
def temperature_converter(a,temVal):
    # pass
    if temVal == 'C':
        celcius(a)
    else:
        Fahrenheit(a)

a = int(input("enter tem. value: "))
ch = str(input("enter scale: "))
temperature_converter(a,ch.upper())


