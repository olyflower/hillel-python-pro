"""Dependency Inversion Principle (DIP).
The last principle called Principle of Dependency Inversion can be separated into two statements.
On the one hand, it indicates that abstractions should not depend on details, since details
should depend on abstractions. On the other hand, it indicates that high-level classes should not depend
on low-level classes, since both should depend on abstractions.
In summary, abstractions should depend on abstractions."""


from abc import ABC, abstractmethod


class Group(ABC):
    @abstractmethod
    def get_subject(self):
        pass


def subject_display(group: Group):
    group.get_subject()


class Teacher(Group):
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def get_subject(self):
        print(self.subject)


teacher = Teacher('John', 21, 'Math')
subject_display(teacher)
