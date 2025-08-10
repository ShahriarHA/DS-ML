# 94. Password Validator: Write a Python program that takes a password as input and checks if it meets the following criteria: at least 8 characters long, contains both uppercase and lowercase letters, and has at least one digit. If the password is valid, print “Password accepted.” If not, use `continue` to prompt the user to enter a valid password.


# Password Validator

while True:
    password = input("Enter your password: ")

    # Check password length
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        continue

    # Check for uppercase
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        continue

    # Check for lowercase
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        continue

    # Check for digit
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        continue

    # If all conditions pass
    print("Password accepted.")
    break
