from homework1.task02 import check_fibonacci


def test_empty_seq_case():
    """Testing that empty sequence returns False"""
    assert not check_fibonacci([])


def test_too_short_seq_case():
    """Testing that sequence with length < 3 returns False"""
    assert not check_fibonacci([1, 1])


def test_seq_with_wrong_first_num_case():
    """Testing that sequence with wrong first num returns False"""
    assert not check_fibonacci([4, 6, 10])


def test_seq_with_wrong_second_num_case():
    """Testing that sequence with wrong second num returns False"""
    assert not check_fibonacci([2, 4, 6])


def test_real_fib_seq_case_list():
    """Testing real fib sequence list returns True"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])


def test_real_fib_seq_case_tuple():
    """Testing real fib sequence tuple returns True"""
    assert check_fibonacci((3, 5, 8, 13, 21, 34, 55, 89))
