# SINGLE INHERITANCE
# SUPER CLASS
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        print(
            f"Welcome {self.first_name} {self.last_name} from parent class"
        )


# SUBCLASS
class Student(Person):
    def __init__(self, first_name, last_name, graduation_year):
        super().__init__(first_name, last_name)
        self.graduation_year = graduation_year

    def display(self):
        super().display()
        print(
            f"Welcome {self.first_name} {self.last_name} "
            f"to the class of {self.graduation_year}"
        )


student1 = Student('Arooj', 'Imran', 2025)
student1.display()


# MULTIPLE INHERITANCE
class Father:
    def driving(self):
        print('Father skill is driving')

class Mother:
    def cooking(self):
        print('Mother skill is cooking')

class Child(Father, Mother):
    def paint(self):
        print("Child skill is painting")


child1 = Child()
child1.driving()
child1.cooking()
child1.paint()


# MULTILEVEL INHERITANCE
class Employee:
    def __init__(self, first_name, last_name, employee_id, department):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.department = department

    def display_details(self):
        print(f"FirstName: {self.first_name}")
        print(f"LastName: {self.last_name}")
        print(f"EmployeeId: {self.employee_id}")


class Manager(Employee):
    def __init__(self, first_name, last_name, role, employee_id, department):
        super().__init__(first_name, last_name, employee_id, department)
        self.role = role

    def display_details(self):
        super().display_details()
        print(f"Employee Department: {self.department}")


class SeniorManager(Manager):
    def __init__(self, first_name, last_name, role, employee_id, department, region):
        super().__init__(first_name, last_name, role, employee_id, department)
        self.region = region

    def display_details(self):
        super().display_details()
        print(f"Employee Region: {self.region}")


senior_manager = SeniorManager("ALI", "Ahmed","Intern", 198, "IT", "Lahore")
senior_manager.display_details()


class A:
    def __init__(self, a):
        self.a = a

    def display(self):
        print(self.a)


class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def display(self):
        super().display()
        print(self.b)


class C(B):
    def __init__(self, a, b, c):
        self.c = c
        super().__init__(a, b)

    def display(self):
        super().display()
        print(self.c)


object1 = C(21, 22, 23)
object1.display()
