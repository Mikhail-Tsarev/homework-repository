from functools import wraps
from typing import Callable


def cache(func: Callable, times: int = None) -> Callable:
    """
    Returns function with cache and
    'times' times only

    :param times:
    :param func: Function for caching
    :return: Function with caching
    """

    cache_data = {}
    i = times

    @wraps(func)
    def wrapper(*args):
        nonlocal i
        if i:
            i -= 1
            if args not in cache_data:
                cache_data[args] = func(*args)
                del cache_data[args]
            i = times - 1
            return cache_data[args]
        return cache_data[args]

    return wrapper


if __name__ == "__main__":

    @cache(times=2)
    def f():
        return input("? ")

    f()
