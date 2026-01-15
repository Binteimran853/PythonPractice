import re
def validate_email():
    while True:
        email = input("Enter your Email: ")
        if re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email):
            return email
        else:
            print("Invalid Email\nTry Again!")

def validate_name():
    while True:
        name = input("Enter your name: ")
        if re.fullmatch(r'[A-Za-z ]+', name):
            return name
        else:
            print("Invalid Name\nTry Again!")

def validate_id():
    while True:
        user_id = input("Enter your ID (it can be alpha-numeric): ")
        if user_id.isalnum():
            return user_id
        else:
            print("Invalid ID\nTry Again!")

def validate_age():
    while True:
        age = (input("Enter your age: "))
        if age.isdigit() and (18 <= int(age) <= 85):
            return int(age)
        else:
            print("Invalid Age\nTry Again!")