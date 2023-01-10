""" 1. Створити frange ітератор, який буде працювати з float.
class frange:
    pass
for i in frange(1, 100, 3.5):
    print(i)"""

from decimal import Decimal


class Frange:
    def __init__(self, start, stop=None, step=None):
        if stop is None:
            stop = start
            start = 0
        if step is None:
            step = 1

        self.start = Decimal(start)
        self.stop = Decimal(stop)
        self.step = Decimal(step)

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.start >= self.stop:
            raise StopIteration
        if self.step < 0 and self.start <= self.stop:
            raise StopIteration

        result = self.start
        self.start += self.step
        return result


assert (list(Frange(5)) == [0, 1, 2, 3, 4])
assert (list(Frange(2, 5)) == [2, 3, 4])
assert (list(Frange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(Frange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(Frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(Frange(1, 5)) == [1, 2, 3, 4])
assert (list(Frange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(Frange(0, 0)) == [])
assert (list(Frange(100, 0)) == [])

print('SUCCESS!')
