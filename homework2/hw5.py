"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g')
== ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p')
== ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2)
== ['p', 'n', 'l', 'j', 'h']
"""

from io import TextIOWrapper
from typing import Any, Iterable, List


def custom_range(
    iterables: Iterable[Any],
    stop_val: Any,
    start_val: Any = None,
    step: int = 1,
) -> List:
    """
    Function accepts any iterable as input data and
    any element from that iterable as a stop value.
    Optional arguments are start value and step.
    Returns processed list of elements.

    :param iterables: Input data
    :param stop_val: Element in iterables to stop before
    :param start_val: Element in iterables to begin with
    :param step: Sequence step
    :return: Resulting list
    """
    if isinstance(iterables, dict):
        iterables = list(iterables)

    if isinstance(iterables, TextIOWrapper):
        iterables = [
            line.strip() for line in iterables.readlines() if line != "\n"
        ]

    if not start_val:
        stop = iterables.index(stop_val)
        return list(iterables[:stop:step])

    stop_val, start_val = start_val, stop_val
    start = iterables.index(start_val)
    stop = iterables.index(stop_val)
    return list(iterables[start:stop:step])
