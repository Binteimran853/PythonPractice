import re
def my_function(name = 'friend'):
    print("Hello", name)

for i in range(4):
    name=input("Enter name (if you don't enter, default name will be used):")
    name=name.strip()
    print(name)
    if re.fullmatch('r[A-Za-z]',name):
        my_function(name)
    else:
        my_function()

def fruits_list():
    return ['apple', 'banana', 'cherry']

print(fruits_list())

def fruits_tuple():
    return (20, 45, 23, 4, 3)

print(fruits_tuple())