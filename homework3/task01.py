from functools import wraps
from typing import Callable


def cashe_times(times: int = None) -> Callable:
    """
    Parametrized decoratoк for cashe function
    Returns cashe 'times' times only

    :param times: Number of times the cashe is returned
    :return: Cashe func
    """

    def cache(func: Callable) -> Callable:
        cache_data = {}
        if times is not None:
            t = times + 1

        @wraps(func)
        def wrapper(*args):
            nonlocal t
            if times is not None:
                t -= 1
                if t < 0:
                    del cache_data[args]
                    t = times
            if args not in cache_data:
                cache_data[args] = func(*args)
            return cache_data[args]

        return wrapper

    return cache
