from homework1.task05 import find_maximal_subarray_sum


def test_normal_case():
    """test normal case"""
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    assert find_maximal_subarray_sum(nums, k) == 16


def test_short_list_case():
    """test 1 number list case"""
    nums = [1]
    k = 3
    assert find_maximal_subarray_sum(nums, k) == 1


def test_short_list_case2():
    """test len(nums) < k  case"""
    nums = [1, 2, -1]
    k = 5
    assert find_maximal_subarray_sum(nums, k) == 3
