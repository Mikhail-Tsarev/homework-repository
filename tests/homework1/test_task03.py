import pytest

from homework1.task03 import find_maximum_and_minimum


def test_normal_file_case():
    """Testing file with line-delimited integers"""
    assert find_maximum_and_minimum("task03_test_file1.txt") == (1, 10)


def test__file_with_empty_strings_case():
    """Testing file with line-delimited integers and empty strings"""
    assert find_maximum_and_minimum("task03_test_file2.txt") == (-4, 20)


def test__file_with_one_int_case():
    """Testing file with only one integer"""
    assert find_maximum_and_minimum("task03_test_file3.txt") == (1, 1)
