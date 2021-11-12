"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Function finds a sub-array with length less equal to k, with max sum

    :param nums: List to process
    :param k: Max length of sub-array
    :return: Max sum of sub-array
    """

    if len(nums) == 0:
        return "Invalid input: empty list"

    current_max = max(nums)
    if k == 1:
        return current_max

    for i in range(2, k + 1):
        for j in range(len(nums)):
            temp_sum = sum(nums[j:j + i])
            if temp_sum > current_max:
                current_max = temp_sum
    return current_max
