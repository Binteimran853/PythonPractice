# SINGLE INHERITANCE
# SUPER CLASS
class Person:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def display(self):
        print(f"Welcome {self.first_name} {self.last_name} from parent class")
# SUBCLASS
class Student(Person):
    def __init__(self,first_name,last_name,graduation_year):
        super().__init__(first_name,last_name)
        self.graduation_year=graduation_year
    def display(self):
        super().display()
        print(f"Welcome {self.first_name} {self.last_name} to the class of {self.graduation_year}")



student1=Student('Arooj','Imran',2025)
student1.display()



# MULTIPLE INHERITANCE
class Father:
    def driving(self):
        print('Father skill is driving')
class Mother:
    def cooking(self):
        print('Mother skill is cooking')
class Child(Father , Mother):
   def paint(self):
       print('Child skill is painting')
child1=Child()
child1.driving()
child1.cooking()
child1.paint()

# MULTILEVEL INHERITANCE
class Employee:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

class A:
    def __init__(self,a):
        self.a=a
    def display(self):
        print(self.a)

class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b
    def display(self):
        super().display()
        print(self.b)

class C(B):
    def __init__(self,a,b,c):
        self.c=c
        super().__init__(a,b)
    def display(self):
        super().display()
        print(self.c)


object1=C(21,22,23)
object1.display()
