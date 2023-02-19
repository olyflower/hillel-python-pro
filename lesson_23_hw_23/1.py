"""Custom Map Function"""


class Map:
    def __init__(self, dict, func1, func2):
        self.dict = dict
        self.keys = iter(dict.keys())
        self.func1 = func1
        self.func2 = func2

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.keys)
        value = self.dict[key]
        return self.func1(key), self.func2(value)


map_example = Map({'A': 1, 'B': 2, 'C': 3}, str.lower, str)

for i in map_example:
    print(i)
