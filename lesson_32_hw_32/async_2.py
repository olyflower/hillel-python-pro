import asyncio
import datetime
import math
import random
import string
import aiohttp
import json


async def get_rates():
    print('get_rates starts')
    async with aiohttp.ClientSession() as session:
        async with session.get('https://bitpay.com/api/rates/') as response:
            data = await response.json()
            with open('rates.json', 'w') as f:
                json.dump(data, f)
            return data


async def in_future_first(future):
    print("in_future_first starts")
    letters = []
    for i in range(50):
        letters.append(random.choice(string.ascii_lowercase))
    print(letters)
    print("in_future_first set result")
    future.set_result(10)


async def current_time_future_first(future):
    print("current_time_future_first starts")
    result = await future
    print(f"Result in_future first: {result}")
    print(f"Current time: {datetime.datetime.now()}")


async def in_future_second(future):
    number = random.randint(1, 100)
    result = math.sqrt(number)
    print(f'sqrt from {number} equal {result}')
    print("in_future_second set result")
    future.set_result(20)


async def text_and_future_second(future, text):
    print("text_and_future_second starts")
    result = await future
    print(f"Result in_future second: {result}")
    print(f'text function complete with text "{text}"')


async def close_event_loop(time_close):
    await asyncio.sleep(time_close)
    event_loop.stop()
    print("Event_loop stopped")


event_loop = asyncio.get_event_loop()
ft_1 = asyncio.Future()
ft_2 = asyncio.Future()

event_loop.create_task(get_rates())
event_loop.create_task(in_future_first(ft_1))
event_loop.create_task(current_time_future_first(ft_1))
event_loop.create_task(in_future_second(ft_2))
event_loop.create_task(text_and_future_second(ft_2, 'Hello!'))
event_loop.create_task(close_event_loop(7))

event_loop.run_forever()
event_loop.close()
