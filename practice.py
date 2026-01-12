class Student:
    id = 22
    name = 'Aqsa'
    role = 'developer'
s1 = Student()
print(s1.id, s1.name, s1.role)
del s1

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
    def __init__(self,id,name,email,order):
        self.id=id
        self.name=name
        self.email=email
        self.order=order
    def __str__(self):
        return f"id: {self.id}  name: {self.name}  email: {self.email}"
    def __add__(self,other):
        print("After adding two objects:",end='')
        return f"id: {self.id+other.id} name: {self.name+other.name}  order: {self.order+other.order}"
    def __sub__(self,other):
        print("After Subtracting two customer's orders:",end='')
        return f"{self.order-other.order}"
    def __mul__(self,other):
        print("After multiply two customer's orders:",end='')
        return f"{self.order * other.order}"
    def __truediv__(self, other):
        print("After division two customer's orders:",end='')
        return f"{self.order/other.order}"
    def __eq__(self,other):
        print("After equality two customer's orders:",end='')
        return isinstance(other,Customer) and (self.order==other.order)
    def __len__(self):
        print(f"Length of 1st customer's email:",end='')
        return len(self.email)



customer1=Customer(1,'Ali','Ali@grayphite.com',12)
customer2=Customer(2,'Aqsa','example123@gmail.com',5)
customer3=Customer(3,'Usama','example123@gmail.com',12)


print(f"{customer1.email} , {customer2.email}")
print(f"Object_1:{str(customer1)} , Object_2:{str(customer2)}")
print(f"{len(customer1)}")
print(f"{customer1 + customer2}")
print(f"{customer1 - customer2}")
print(f"{customer1*customer3}")
print(f"{customer1==customer3}")
print(f"{customer1/customer2}")

