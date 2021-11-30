import functools
from typing import Callable


def save_info(original_func: Callable) -> Callable:
    """Decorator which saves original
    function doc and name attributes

    :param original_func: Function for saving its info"""

    def wraps(wrapping_func: Callable) -> Callable:
        wrapping_func.__doc__ = original_func.__doc__
        wrapping_func.__name__ = original_func.__name__
        wrapping_func.__original_func = original_func
        return wrapping_func

    return wraps


def print_result(func):
    @save_info(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper
