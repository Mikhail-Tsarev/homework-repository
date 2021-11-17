import pytest

from homework3.task04 import is_armstrong

test_data = [(153, True), (5, True), (11, False), (13, False)]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_is_armstrong(test_input, expected):
    assert is_armstrong(test_input) == expected
