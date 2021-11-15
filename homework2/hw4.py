"""
Write a function that accepts another function
as an argument. Then it should return such a function,
so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""

from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    """
    Returns function with cache

    :param func: Function for caching
    :return: Function with caching
    """
    _cache = {}

    @wraps(func)
    def wrapper(*args):
        try:
            return _cache[args]
        except KeyError:
            _cache[args] = func(*args)
            return _cache[args]

    return wrapper
