""" 3. Реалізувати метод square в фігурах які залишилися. (Triangle+Parallelogram).
Triangle - треба створити клас"""

import math


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, x, y, side, height):
        super().__init__(x, y)
        self.side = side
        self.height = height

    def square(self):
        return (self.side * self.height) / 2


class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Parallelogram(Rectangle):
    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def square(self):
        return self.height * self.width * math.sin((self.angle * math.pi) / 180)


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass


c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)

t = Triangle(1, 2, 50, 10)
t1 = Triangle(1, 2, 4.5, 1)

r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, 50, 20)
r2 = Rectangle(0, 20, 100, 20)

p = Parallelogram(1, 2, 20, 30, 90)
p1 = Parallelogram(1, 2, 4, 100, 45)

scene = Scene()
scene.add_figure(c)
scene.add_figure(c1)
scene.add_figure(t)
scene.add_figure(t1)
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(p)
scene.add_figure(p1)

scene.total_square()
print(c.square())
print(c1.square())
print(t.square())
print(t1.square())
print(r.square())
print(r1.square())
print(r2.square())
print(p.square())
print(p1.square())

print(scene.total_square())
