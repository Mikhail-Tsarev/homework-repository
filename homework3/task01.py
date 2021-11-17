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

    _cache = {}
    i = times

    @wraps(func)
    def wrapper(*args):
        nonlocal i
        try:
            if i:
                i -= 1
                return _cache[args]
            del _cache[args]
            i = times - 1
            return _cache[args]
        except KeyError:
            _cache[args] = func(*args)
            return _cache[args]

    return wrapper


if __name__ == "__main__":

    @cache(times=2)
    def f():
        return input("? ")

    f()
