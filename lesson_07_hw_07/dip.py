"""Dependency Inversion Principle (DIP).
The last principle called Principle of Dependency Inversion can be separated into two statements.
On the one hand, it indicates that abstractions should not depend on details, since details
should depend on abstractions. On the other hand, it indicates that high-level classes should not depend
on low-level classes, since both should depend on abstractions.
In summary, abstractions should depend on abstractions."""

# Принцип інверсіі залежностей - верхні класи не повінні залежати від нижніх класів.
# Клас Person має функцію get_status, вона незалежна від класів Teacher і Student.
# get_status приймає параметром клас Teacher чи Student та прінтує результат.


class Person:

    def get_status(self, note, **kwargs):
        note(*kwargs).get_status()


class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def get_status(self):
        print(f'Teacher, subject - {self.subject}')


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def get_status(self):
        print(f'Student, course - {self.course}')


person = Person()
student = Student('Mike', 21, 4)
teacher = Teacher('Helen', 35, 'Math')
person.get_status(Student, name='Mike', age=21, course=4)
person.get_status(Teacher, name='Helen', age=35, subject='Math')
