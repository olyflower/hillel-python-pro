"""Open-Closed Principle (OCP).
Classes should be open for extension, but closed for modification.
In other words, the code should be written in such a way that, when adding new functionality,
previously written code, which may be in use by other users, should not be modified.
"""
from datetime import date, time


class Teacher:
    def __init__(self, name, exam):
        self.name = name
        self.exam = exam

    def exam_information(self):
        return f'Exam: {self.exam}, current date: {date.today()}'


class Student:
    def __init__(self, name, course):
        self.name = name
        self. course = course

    def get_course(self):
        return f'Course of the student {self.name}: {self.course}'

    def get_name(self):
        return f'Name of the teacher: {self.name}'


class Group(Teacher):
    def __init__(self, name, exam):
        super().__init__(name, exam)

    def exam_information(self):
        return f'Exam: {self.exam}, current date: {date.today()}, the teacher: {self.name}'


group = Group('Mike', 'Science')
print(group.exam_information())
teacher = Teacher('Helen', 'Math')
teacher1 = Teacher('Rob', 'History')
