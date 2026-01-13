def sum_of_numbers(*numbers):
    for number in numbers:
        print(number[])

def my_function(greeting,*names):
    for name in names:
        print(f"greeting {name}")
my_function('Hello','Aqsa','Ali','Amina','Aasq','Mahnoor')