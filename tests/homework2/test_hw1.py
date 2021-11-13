from homework2.hw1 import check_power_of_2


def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)
