class Student:
    id = 22
    name = 'Aqsa'
    role = 'developer'


student1 = Student()
print(student1.id, student1.name, student1.role)
del student1



#   EMPTY CLASSES FOR ADDING DYNAMIC ATTRIBUTES
class Users:
    pass


user = Users()
print(user)
user.name = 'Usama Imran'
user.role = 'Senior Software Engineer'
print(user.name, end=' ')
print(user.role)


# PRACTICE DUNDER(DOUBLE UNDERSCORE METHODS) METHODS
class Customer:
    def __init__(self, id, name, email, order):
        self.id = id
        self.name = name
        self.email = email
        self.order = order

    def __str__(self):
        return f"id: {self.id}  name: {self.name}  email: {self.email}"

    def __add__(self, other):
        return (
            f"id: {self.id + other.id} "
            f"name: {self.name + other.name} "
            f"order: {self.order + other.order}"
        )

    def __sub__(self, other):
        return f"{self.order - other.order}"

    def __mul__(self, other):
        return f"{self.order * other.order}"

    def __truediv__(self, other):
        return f"{self.order / other.order}"

    def __eq__(self, other):
        return isinstance(other, Customer) and (self.order == other.order)

    def __len__(self):
        return len(self.email)



customer1 = Customer(1,'Ali','Ali@grayphite.com',12)
customer2 = Customer(2,'Aqsa','example123@gmail.com',5)
customer3 = Customer(3,'Usama','example123@gmail.com',12)


print(f"{customer1.email} , {customer2.email}")
print(f"Object_1:{str(customer1)} \n Object_2:{str(customer2)}")
print("Length of Customer's email: ", end='')
print(f"{len(customer1)}")
print("Perform addition on two objects: ", end='')
print(f"{customer1 + customer2}")
print("Perform subtraction on two objects: ", end='')
print(f"{customer1 - customer2}")
print("Perform multiplication on two objects: ", end='')
print(f"{customer1 * customer3}")
print("Perform equality on two objects: ", end='')
print(f"{customer1 == customer3}")
print("Perform division on two objects: ", end='')
print(f"{customer1 / customer2}")

