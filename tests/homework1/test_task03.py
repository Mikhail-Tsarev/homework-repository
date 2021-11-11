import pytest

from homework1.task03 import find_maximum_and_minimum


def test_empty_seq_case():
    """Testing that empty sequence returns False"""
    assert not find_maximum_and_minimum([])
