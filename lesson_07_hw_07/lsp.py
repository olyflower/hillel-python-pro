"""Liskov Substitution Principle (LSP).
Liskov’s Principle of Substitution states that classes should be substitutable by instances of their subclasses.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def get_name(self):
        return f'Name of the teacher: {self.name}'


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
        self.marks = []

    def display(self):
        return f'Student name: {self.name}'

    def add_mark(self, mark):
        self.marks.append(mark)


student = Student('Mark', 20, 3)
teacher = Teacher('Helen', 35, 200)
student1 = Student('Den', 21, 4)
teacher1 = Teacher('Rob', 45, 350)
persons = (student, student1, teacher, teacher1)

for person in persons:
    if person.age > 20:
        print(person.name)
