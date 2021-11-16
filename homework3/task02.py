import hashlib
import multiprocessing as mp
import random
import struct
import time


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


if __name__ == "__main__":
    args = range(500)
    pool = mp.Pool(60)
    result = pool.map(slow_calculate, args)
    print(sum(result))
