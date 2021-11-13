from homework2.hw3 import combinations


def test_3_lists_case():
    """Testing with 3 lists as args"""

    assert combinations([1, 2], [3, 4], [5, 6]) == [
        [1, 3, 5],
        [1, 3, 6],
        [1, 4, 5],
        [1, 4, 6],
        [2, 3, 5],
        [2, 3, 6],
        [2, 4, 5],
        [2, 4, 6],
    ]
