import re
from validators import (
    validate_email,
    validate_name,
    validate_id,
    validate_age)


def greet_user(name='friend'):
    print("Hello", name)

for _ in range(4):
    name = input("Enter your name:(If not enter default name will be used) ").strip()
    name = name.replace(" ","")
    if not name:
        greet_user()
    elif re.match(r"^[A-Za-z ]+$", name):
        greet_user(name)
    else:
        greet_user()


person={
    'Name' : "Aqsa Imran",
    'Role' : "Developer",
    'Email' : "aqsaimran341@gmail.com",
}
def person_details(person): #Time & Space Complexity O(1)
    print(f"Name: {person['Name']}, "
          f"Role: {person['Role']}, "
          f"Email: {person['Email']}"
          )

person_details(person)


"""CHECKING THAT POSITIONAL ARGUMENTS MUST COME FIRST FROM KEYWORD ARGUMENTS"""
def my_function(name, role, email):
    return {
        'name' : name,
        'role' : role,
        'email' : email
    }

print(my_function('Aqsa', role = 'IT Developer', email = 'aqsaimran341@gmail.com'))

"""
PRACTICE ON *args
"""
def arbitrary_test_function(greeting, *names): #Time & Space Complexity O(n)
    for name in names:
        print(greeting, name )

arbitrary_test_function('Hi,',"Hassan", "Ali", "Arslan", "Javaid")


"""PRACTICE REAL WORLD EXAMPLE FOR ARBITRARY ARGUMENTS"""
def generate_bill(customer_name, service_charge_percent, *items_prices): # Time & Space: O(n)
    """
    name = must be a valid string
    service charge persent = must be float or int type
    item_prices = must be valid int or float numbers
    Time and Space complexity is O(1) for isinstance() because python stores type pointer internally.
    """
    print(f"items_prices: {type(items_prices)}")

    if not isinstance(customer_name, str) or not customer_name.strip():
        raise ValueError("Customer Name must be a valid string.")
    if not isinstance(service_charge_percent, (float, int)) or not service_charge_percent > 0:
        raise ValueError("Service Charge Persent must be a non-negative number")
    if not all ((isinstance(price,(float, int)) and price >= 0) for price in items_prices):
        raise ValueError("Items Prices must be a non-negative number")

    sub_total=sum(items_prices)
    service_charge = sub_total * (service_charge_percent / 100)
    total_amount = sub_total + service_charge
    print(f"==== Bill for {customer_name} ====")
    for i, item in enumerate(items_prices, start = 1):
            print(f"Item {i}: ${item:.2f}")
    return (
            f"service_charge {service_charge_percent}%: ${service_charge:.2f}\n"
            f"total_amount: ${total_amount:.2f}"
            )

item_prices = []
while True:
   try:
       n=int(input("How many items you want to add?: "))
       if n <= 0:
           print("Please enter a positive integer")
           continue
       break
   except ValueError:
       print("Please enter a non-negative number")

for i in range(1, n + 1):
   while True:
       try:
           price= float(input(f"Enter Price for item {i}: "))
           if price < 0:
               print("Price must be non-negative number")
               continue
           item_prices.append(price)
           break
       except ValueError:
           print("Price must be a number")
print(generate_bill('Hafiz Muavia', 10,*item_prices))

def create_user_profile(**kwargs):
    if 'name' not in kwargs or 'ID' not in kwargs:
        raise ValueError("Name and ID filed required")
    print("=== User's Profile ===")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

    return kwargs

try:
    name = validate_name()
    ID = validate_id()
    Email = validate_email()
    age = validate_age()
    role = input("Enter your role: ")
    country = input("Enter your country: ")
    skills = input("Enter your skills by seprated by space: ").strip().split()

    profile = create_user_profile(
        ID = ID,
        name = name,
        Email = Email,
        age = age,
        role = role,
        country = country,
        skills = skills
    )
except ValueError as e:
    print('Error:', e)
