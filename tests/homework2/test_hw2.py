from homework2.hw2 import major_and_minor_elem


def test_list_of_num_case1():
    """Testing that function returns most and least
    common elements from list of positive ints"""

    lst = [3, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 5, 5]
    result = (1, 3)
    assert major_and_minor_elem(lst) == result


def test_list_of_num_case():
    """Testing that function returns most and least
    common elements from list of negative ints"""

    lst = [-2, -2, -1, -1, -1, -1, -1, -1, -2, -2]
    result = (-1, -2)
    assert major_and_minor_elem(lst) == result


def test_list_of_letters_case():
    """Testing that function returns most and least
    common elements from list of letters"""

    lst = ["a", "b", "b", "a", "a", "a", "a", "z", "s", "s", "a"]
    result = ("a", "z")
    assert major_and_minor_elem(lst) == result


def test_list_of_mixed_case():
    """Testing that function returns
    most and least common elements from mixed list"""

    lst = [
        "a",
        "b",
        "b",
        1,
        1,
        6,
        6,
        6,
        "a",
        "a",
        "a",
        "a",
        "a",
        0,
        "a",
        "a",
    ]
    result = ("a", 0)
    assert major_and_minor_elem(lst) == result
