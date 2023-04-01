"""1 Написати асинхронну функцію. Вимоги:
    1. Більше 5 корутин
    2. Одна корутина завершує івент луп
    3. Дві корутини використовують фючерси
    4. Не використовувати сліп"""

import asyncio
import datetime
import random
import string


async def get_letters():
    print('get_letter starts')
    await asyncio.sleep(1)
    letters = []
    for i in range(5):
        letters.append(random.choice(string.ascii_lowercase))
    print(letters)


async def in_future_1(future):
    await asyncio.sleep(1)
    print("in_future_1 set result")
    future.set_result(10)


async def current_time_future_1(future):
    result = await future
    print(result)
    await asyncio.sleep(2)
    print(f"Current time: {datetime.datetime.now()}")


async def in_future_2(future):
    await asyncio.sleep(1)
    print("in_future_2 set result")
    future.set_result(20)


async def func_3(future, text):
    result = await future
    print(result)
    await asyncio.sleep(2)
    print(f'func_3 complete with text "{text}"')


async def close_event_loop(time_close):
    await asyncio.sleep(time_close)
    event_loop.stop()

event_loop = asyncio.get_event_loop()
ft_1 = asyncio.Future()
ft_2 = asyncio.Future()

event_loop.create_task(get_letters())
event_loop.create_task(in_future_1(ft_1))
event_loop.create_task(current_time_future_1(ft_1))
event_loop.create_task(in_future_2(ft_2))
event_loop.create_task(func_3(ft_2, 'Hello!'))
event_loop.create_task(close_event_loop(8))

event_loop.run_forever()
event_loop.close()
