"""1. Реалізувати LFU алгоритм для кешування. За базу берем існуючий декоратор.
Написати для фетчування юерелів. Додати можливість указати максимум елементів в кеші."""

import functools
from collections import OrderedDict
import requests


def cache(max_limit=64):
    """Декоратор реалізування LFU алгоритма для кешування.
    """
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))

            if cache_key in deco._cache:

                deco._cache[cache_key]['counter'] += 1
                # переносимо в кінець списку
                deco._cache.move_to_end(cache_key, last=True)
                return deco._cache[cache_key]['content']
            result = f(*args, **kwargs)

            # створюємо словник з лічильником і контентом
            deco._cache[cache_key] = {'counter': 0, 'content': result}
            print(deco._cache)

            # видаляємо якшо досягли ліміта
            if len(deco._cache) >= max_limit:
                # видаляємо елемент,який був найменш часто використаний
                del deco._cache[min(deco._cache, key=lambda item: deco._cache[item]['counter'])]
            return result

        deco._cache = OrderedDict()
        return deco
    return internal


@cache(max_limit=2)
def fetch_url(url, first_n=100):
    """Fetch a given url.
    """
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://youtube.com')
fetch_url('https://youtube.com')
