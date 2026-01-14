# import re
# def my_function(name = 'friend'):
#     print("Hello", name)
#
# for i in range(4):
#     name=input("Enter name (if you don't enter, default name will be used):")
#     name=name.strip()
#     print(name)
#     if re.fullmatch('r[A-Za-z]',name):
#         my_function(name)
#     else:
#         my_function()

def person_details(person):
    print(f"Name: {person["Name"]}, "
          f"Role: {person["Role"]}, "
          f"Email: {person["Email"]}"
          )
person={
    'Name' : "Aqsa",
    'Role' : "Developer",
    'Email' : "aqsaimran341@gmail.com",
}
person_details(person)
def my_function(name, role, email):
    return {
        'name' : name,
        'role' : role,
        'email' : email
    }
print(my_function('Aqsa', role = 'IT Developer', email = 'aqsaimran341@gmail.com'))

def arbitrary_test_function(greeting, *names):
    for name in names:
        print(greeting, name )

arbitrary_test_function('Hi,',"Hassan", "Ali", "Arslan", "Javaid")

# PRACTICE REAL WORLD EXAMPLE FOR ARBITRARY ARGUMENTS
def generate_bill(customer_name, service_charge_persent, *items_prices):
    """
    name = must be a valid string
    service charge persent = must be float or int type
    item_prices = must be valid int or float numbers
    """
    print(f"items_prices: {type(items_prices)}")
    if not isinstance(customer_name,str) or not customer_name.strip():
        raise ValueError("Customer Name must be a valid string.")
    if not isinstance(service_charge_persent, (float, int)) or not service_charge_persent > 0:
        raise ValueError("Service Charge Persent must be a non-negative number")
    if not all ((isinstance(price,(float, int)) and price >= 0) for price in items_prices):
        raise ValueError("Items Prices must be a non-negative number")
    sub_total=sum(items_prices)
    service_charge = sub_total * (service_charge_persent / 100)
    total_amount = sub_total + service_charge
    print(f"==== Bill for {customer_name} ====")
    for i, item in enumerate(items_prices, start = 1):
            print(f"Item {i}: ${item:.2f}")
    return (
                f"service_charge {service_charge_persent}%: ${service_charge:.2f}\n"
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
               print("Price mut be non-negative number")
               continue
           item_prices.append(price)
           break
       except ValueError:
           print("Price must be a number")
print(generate_bill('Hafiz Muavia', 10,*item_prices))

# def keyword_arbitrary_arguments_test_function(greeting, **names):
