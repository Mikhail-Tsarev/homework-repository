from functools import wraps
from typing import Callable


def cashe_times(times: int = None) -> Callable:
    def cache(func: Callable) -> Callable:
        cache_data = {}
        t = times + 1

        @wraps(func)
        def wrapper(*args):
            nonlocal t
            if times is not None:
                t -= 1
                if t == 0:
                    del cache_data[args]
                    t = times

            if args not in cache_data:
                cache_data[args] = func(*args)
            return cache_data[args]

        return wrapper

    return cache


if __name__ == "__main__":

    @cashe_times(3)
    def f():
        return input("? ")

    for i in range(10):
        print(f())
