"""
Given a cell with "it's a fib sequence" from slideshow,
please write function "check_fib", which
accepts a Sequence of integers, and
returns if the given sequence is a
Fibonacci sequence
We guarantee, that the given sequence
contain >= 0 integers inside.
"""
from math import sqrt
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """Check if a sequence of integers is a Fibonacci sequence"""

    def is_fib_num(n: int) -> bool:
        """Check if number is a Fib number"""
        a = (0.5 + 0.5 * sqrt(5.0)) * n
        return n == 0 or abs(round(a) - a) < 1.0 / n

    # one number is not a sequence
    if len(data) < 2:
        return False

    # check if the first and the second ints in a sequence
    # are fib numbers, because if not we no need to continue
    if not is_fib_num(data[0]) or not is_fib_num(data[1]):
        return False

    # for 2 nums sequence case
    if len(data) == 2:
        x = data[1] - data[0]
        if x <= data[0] and is_fib_num(x):
            return True
        return False

    # for other cases
    while len(data) > 2:
        if not (data[0] + data[1] == data[2]):
            return False
        data = data[1:]
    return True
