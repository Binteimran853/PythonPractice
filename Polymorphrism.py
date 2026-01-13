class Car:
   def __init__(self, model, brand):
       self.model = model
       self.brand = brand

   def mov(self):
       print("Car is moving")


class Boat:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def mov(self):
        print("Boat is sailing")


class Plan:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def mov(self):
        print("Plan is flying")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plan1 = Plan("Boeing", "747")
for x in (car1, boat1, plan1):
    x.mov()


#   polymorphism with inheritance
class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def show(self):
        return f"Person Data"


class Customer(Person):
    def show(self):
        return f"Customer Data"


class Employee(Person):
    def show(self):
        return f"Employee Data"


person1 = Person(2, "Ali", 18)
customer1 = Customer(3, "Peeter", 18)
employee1 = Employee(3, "Harry", 19)
for x in (person1, customer1, employee1):
    print(f"===={x.show()}====")
    print(x.id, x.name, x.age)
