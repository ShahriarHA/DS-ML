# 109. Greeting Generator: Write a Python function called `greeting_generator` that takes a name as input and returns a greeting message using nested functions. The greeting message should be customizable (e.g., “Hello, {name}! How are you today?”).
def messagePrint(a):
    # pass
    print(a)
def greeting_generator(a):
    # pass
    aa = f"Hello {a}! How are you today?"
    messagePrint(aa)
    
name = str(input("enter your name: "))

greeting_generator(name)
 


