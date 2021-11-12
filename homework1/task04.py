"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such
that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length
of N where 0 ≤ N ≤ 1000.
"""

from itertools import product
from typing import List


def check_sum_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int]
) -> int:
    """
    Counts how many tuples (i, j, k, l) there are such
    that A[i] + B[j] + C[k] + D[l] is zero

    :param a: List to process
    :param b: List to process
    :param c: List to process
    :param d: List to process
    :return: Number of tuples with zero sum
    """

    count = 0
    lst = product(a, b, c, d)
    for nums in lst:
        if sum(nums) == 0:
            count += 1
    return count
