"""2. Створити декоратор для заміру пам'яті."""

import psutil
import functools


def measure_memory(f):
    """ Декоратор для замірювання витраченої пам'яті.
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        process = psutil.Process()
        before = process.memory_info().rss
        result = f(*args, **kwargs)
        after = process.memory_info().rss
        print(f'Used memory - {(after - before) / 1024} MB')
        return result
    return wrapper


@measure_memory
def add(a, b):
    res = a + b
    return res


add(1, 2)
