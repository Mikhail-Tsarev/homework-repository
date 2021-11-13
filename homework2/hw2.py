"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """
    Returns most common and least common elements in list

    :param inp: List of elements
    :return: Most and least common elements
    """

    counter = Counter(inp)
    el_in_order = counter.most_common()
    return el_in_order[0][0], el_in_order[-1][0]


if __name__ == "__main__":
    lst = [-2, -2, -1, -1, -1, -1, -1, -1, -2, -2]
    print(major_and_minor_elem(lst))
