class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.__grade = None

    def set_grade(self):
        while True:
            try:
                grade=int(input('Enter Grade:'))
                if grade>=0 and grade<=100:
                    self.__grade=grade
                    break
                else:
                    print("Grade must be between 0 and 100. Try again.")
            except ValueError:
                print("Enter a valid number")
    def get_result(self):
        if self.__grade < 60:
            return f"Student Failed (Grade: {self.__grade})"
        else:
            return f"Student Passed (Grade: {self.__grade})"


student1 = Student(12, "Ali", 34)
student1.set_grade()
print(student1.get_result())
