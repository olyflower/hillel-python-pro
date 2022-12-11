""" Point(1, 2) in Circle(1, 2, 10) -> True or False
p1 in c1 -> True or False. """


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __contains__(self, point):
        return (point.x - self.x) ** 2 + (point.y - self.y) ** 2 <= self.r ** 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(-200, -500)
c = Circle(100, 50, 200)

print(p in c)
print(Point(1, 2) in Circle(1, 2, 10))
