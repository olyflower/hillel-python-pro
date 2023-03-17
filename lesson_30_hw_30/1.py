import os
import random
import string
import time
from multiprocessing.pool import ThreadPool

import requests

workers = 256
DATA_SIZE = 10


def fetch_pic(num_pic):
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), 'img')
    for _ in range(num_pic):
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'{path}/{random_name}.jpg', 'wb') as f:
                f.write(response.content)


start = time.time()
with ThreadPool(workers) as pool:
    input_data = [DATA_SIZE // workers for _ in range(workers)]
    pool.map(fetch_pic, input_data)
print(time.time() - start)


workers_list_10 = [1, 2, 4, 8, 16, 20, 25, 256]
result_list_10 = [7.8, 6.4, 2.3, 2.1, 0.004, 0.003, 0.004, 0.24]
