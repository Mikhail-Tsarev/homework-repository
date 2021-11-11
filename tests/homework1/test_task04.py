import pytest

from homework1.task04 import check_sum_of_four


def test_normal_case():
    """Testing normal case"""
    a = [0, 1]
    b = [0, 1]
    c = [0, 1]
    d = [0, 1]
    assert check_sum_of_four(a, b, c, d) == 1


def test_all_nums_are_positives_case():
    """Testing all pos case"""
    a = [1, 2]
    b = [3, 4]
    c = [5, 6]
    d = [7, 8]
    assert check_sum_of_four(a, b, c, d) == 0


def test_all_nums_are_negative_case():
    """Testing all pos case"""
    a = [-1, -2]
    b = [-3, -4]
    c = [-5, -6]
    d = [-7, -8]
    assert check_sum_of_four(a, b, c, d) == 0


def test_all_nums_are_zeros_case():
    """Testing all pos case"""
    a = [0, 0, 0, 0]
    b = [0, 0, 0, 0]
    c = [0, 0, 0, 0]
    d = [0, 0, 0, 0]
    assert check_sum_of_four(a, b, c, d) == len(a) ** 4


def test_empty_lists_case():
    """Testing all pos case"""
    a = []
    b = []
    c = []
    d = []
    assert check_sum_of_four(a, b, c, d) == 0
