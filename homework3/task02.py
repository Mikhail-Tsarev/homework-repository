import hashlib
import multiprocessing as mp
import random
import struct
import time
from typing import Any, Callable, Sequence


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def multi_process_func(
    func: Callable, func_arg: Sequence[Any], pools: int = 60
) -> int:
    """
    Returns the sum of the results of parallel calculations
    of a slow calculation function executed with different arguments

    :param func: Slow function to run in parallel processes
    :param func_arg: Slow function arg
    :param pools: Number of parallel processes
    :return: Sum of parallel calculation
    """

    with mp.Pool(pools) as pool:
        result = sum(pool.map(func, func_arg))
    return result
