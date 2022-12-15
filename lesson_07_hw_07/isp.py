"""Interface Segregation Principle (ISP).
The Interface Segregation Principle states that clients should not be forced to rely on methods
they do not use and therefore suggests the creation of specific interfaces or classes for such clients.
"""

# Краще мати багато маленьких інтерфейсів, ніж один великий.
# Отже, маємо класи Talk, Salary, Grants.
# Клас Teacher наслідується від класів Talk, Salary,
# класс Student наслідується від класів Talk, Grant,
# таким чином виконується принцип поділу інтерфейсів.


class Talk:
    def __init__(self, name):
        self.name = name

    def talk(self):
        return f'Hello! My name is {self.name}'


class Salary:
    def __init__(self, salary):
        self.salary = salary

    def display_salary(self):
        return f'Salary - {self.salary}'


class Grants:
    def __init__(self, grant):
        self.grant = grant

    def display_grant(self):
        return f'Grant - {self.grant}'


class Teacher(Talk, Salary):
    def __init__(self, name, age, salary):
        super().__init__(name)
        self.name = name
        self.age = age
        self.salary = salary

    def get_age(self):
        return f'Age of the teacher {self.name}: {self.age}'


class Student(Talk, Grants):
    def __init__(self, name, age, course, grant):
        super().__init__(name)
        self.name = name
        self.age = age
        self.course = course
        self.grant = grant

    def get_course(self):
        return f'Course of the student {self.name}: {self.course}'


student = Student('Mark', 20, 3, 100)
teacher = Teacher('Helen', 35, 200)
student1 = Student('Den', 21, 4, 150)
teacher1 = Teacher('Rob', 45, 350)

print(teacher.talk())
print(student.talk())
print(student1.display_grant())
print(teacher1.display_salary())
print(teacher.get_age())
print(student1.get_course())
