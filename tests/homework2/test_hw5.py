import string

from homework2.hw5 import custom_range


def test_with_strings_case1():
    """Testing with string and stop letter as args"""

    assert custom_range(string.ascii_lowercase, "g") == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]


def test_with_strings_case2():
    """Testing with string start and stop letters as args"""

    assert custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]


def test_with_strings_case3():
    """Testing with string start and stop letters and step as args"""

    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]


def test_with_tuple_case():
    """Testing with string start and stop integers as args"""
    nums = (11, 22, 33, 44, 55, 66, 77, 88, 99)
    assert custom_range(nums, 22, 88, 2) == [22, 44, 66]


def test_with_dict_case():
    """Testing with dict and dict keys as args"""
    d = {1: "aa", 2: "bb", 3: "cc", 4: "dd", 5: "ee"}
    assert custom_range(d, 2, 5) == [2, 3, 4]


def test_with_file_case():
    """Testing with txt file and letters as args"""
    file_name = "./tests/homework2/data_hw5.txt"
    with open(file_name) as fi:
        assert custom_range(fi, "a", "b") == ["a", "2", "3", "4", "5"]
