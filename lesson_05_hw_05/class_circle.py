""" Створити клас Circle(x,y,radius). Додати метод contains.
 Цей метод приймає екземпляр класу Point(x,y). Цей метод має повертати
 True or False. Якшо точка в колі, то True якшо поза колом, то False."""


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def contains(self, point):
        return (point.x - self.x) ** 2 + (point.y - self.y) ** 2 <= self.r ** 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


circle = Circle(1, 3, 50)
point_one = Point(-10, 10)
print(circle.contains(point_one))
