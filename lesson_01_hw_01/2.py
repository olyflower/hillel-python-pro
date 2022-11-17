"""2. Створити декоратор для заміру пам'яті."""

import os
import psutil
import functools


def process_memory():
    """Функція для отримання інформації про пам’ять процесу.
    """
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def measure_memory(f):
    """ Декоратор для замірювання витраченої пам'яті.
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        before = process_memory()
        result = f(*args, **kwargs)
        after = process_memory()
        print(before, after)
        print(f'Used memory - {after - before}')
        return result
    return wrapper


@measure_memory
def add(a, b):
    res = a + b
    return res


add(1, 2)
