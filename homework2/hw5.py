"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""

import string
from typing import Any, Iterable, List


def custom_range(
    iterables: Iterable[Any],
    stop_val: Any,
    start_val: Any = None,
    step: int = 1,
) -> List:
    """

    :param iterables: Input data
    :param stop_val: Element in iterables to stop before
    :param start_val: Element in iterables to begin with
    :param step: Sequence step
    :return: The resulting list
    """

    if not start_val:
        stop = iterables.index(stop_val)
        return list(iterables[:stop:step])

    stop_val, start_val = start_val, stop_val
    start = iterables.index(start_val)
    stop = iterables.index(stop_val)
    return list(iterables[start:stop:step])


print(custom_range(string.ascii_lowercase, "g"))
print(custom_range(string.ascii_lowercase, "g", "p"))
print(custom_range(string.ascii_lowercase, "p", "g", -2))
print(custom_range((11, 22, 33, 44, 55, 66, 77, 88, 99), 22, 77))
print(custom_range((11, 22, 33, 44, 55, 66, 77, 88, 99), 77))
print(custom_range((11, 22, 33, 44, 55, 66, 77, 88, 99), 22, 77, 2))
s = {1: "aa", 2: "bb", 3: "ff"}
