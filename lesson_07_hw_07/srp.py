"""Single Responsibility Principle (SRP).
Class should be responsible for only one functionality.
In other words, the class should only have a single reason to change.
"""


class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def get_subject(self):
        return f'Subject of the student {self.name}: {self.subject}'


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self. course = course

    def get_course(self):
        return f'Course of the student {self.name}: {self.course}'

    def get_name(self):
        return f'Name of the teacher: {self.name}'

# Класи повинні мати одну відповідальність, тому створимо окремий класс UniversityDataBase, який буде відповідати
# за збереження даних в базі даних.


class UniversityDataBase:
    @staticmethod
    def save(person, filename):
        with open(filename, 'a', encoding='UTF8') as f:
            f.write(person.name)


student = Student('Mark', 21, 3)
student1 = Student('Den', 22, 2)
student2 = Student('Helen', 19, 4)
teacher = Teacher('Robert', 40, 'Math')
teacher1 = Teacher('Rob', 35, 'History')

UniversityDataBase.save(student, 'db.txt')
UniversityDataBase.save(student1, 'db.txt')
UniversityDataBase.save(student2, 'db.txt')
UniversityDataBase.save(teacher, 'db.txt')
UniversityDataBase.save(teacher1, 'db.txt')
