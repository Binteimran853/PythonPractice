user_input = input("Enter number student marks separated by ',':").split(',')
marks_list = user_input
print(f" Student Marks List: {marks_list}, type:{type(marks_list)} ")
print(f"Marks in form of tuple:{tuple(marks_list)} , type: {type(tuple(marks_list))}")

fruits = ["apple", "banana", "cherry", "kiwi", "mango","orange","Peach","Gava","Fruiter"]
new_list = [x.upper() for x in fruits if 'r' in x]
print(new_list)
