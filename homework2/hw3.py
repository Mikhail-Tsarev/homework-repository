"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""

from itertools import product
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """
    Function returns all possible combinations with length K from K lists,
    where the first element is from the first list,
    the second is from the second and so one

    :param args: K Lists of arguments
    :return: List of lists of lengths K with any possible combinations
    """

    return [list(x) for x in product(*args)]
