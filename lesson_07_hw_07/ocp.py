"""Open-Closed Principle (OCP).
Classes should be open for extension, but closed for modification.
In other words, the code should be written in such a way that, when adding new functionality,
previously written code, which may be in use by other users, should not be modified.
"""


class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        return f'Hello, my name is {self.name}'


class Student(SchoolMember):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def tell(self):
        return f'Hello, i am a student of the {self.course}, my name is {self.name}'


class Teacher(SchoolMember):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def tell(self):
        return f'Hello, i am a teaching {self.subject}, my name is {self.name}'

# можна розширити клас SchoolMember та додати class Nurse, цей клас успадковується також від SchoolMember
# та використовує його методи, змінюючи їх у контексті вимог свого класу.


class Nurse(SchoolMember):
    def __init__(self, name, age, phone_number):
        super().__init__(name, age)
        self.phone_number = phone_number

    def tell(self):
        return f'Hello, i am a school nurse, my name is {self.name}, phone number: {self.phone_number}'


student = Student('Mark', 21, 4)
teacher = Teacher('Helen', 35, 'Math')
nurse = Nurse('Marta', 36, 1213332)

print(student.tell())
print(teacher.tell())
print(nurse.tell())
