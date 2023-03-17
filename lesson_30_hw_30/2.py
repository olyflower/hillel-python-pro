import multiprocessing
import random
import time


DATA_SIZE = 1_000_000
lst = []
workers = 100

start_time = time.time()


def fill_data(n):
    while n > 0:
        n -= 1
        lst.append(random.randint(1, 100))


start = time.time()
with multiprocessing.Pool(workers) as pool:
    input_data = [DATA_SIZE // workers for _ in range(workers)]
    pool.map(fill_data, input_data)
print(time.time() - start)


w = [1, 2, 4, 8, 16, 18, 20, 23, 32, 64, 128, 256, 512]
res = [0.56, 0.30, 0.19, 0.17, 0.16, 0.15, 0.14, 0.15, 0.16, 0.18, 0.24, 0.34, 0.65]
