from homework9.hw2 import Suppressor, suppressor


def test_func_suppressor():
    """Testing that with suppressor func
    exception is suppressed"""

    with suppressor(IndexError):
        assert [][2]


def test_class_suppressor():
    """Testing that with suppressor class
    exception is suppressed"""

    with Suppressor(IndexError):
        assert [][2]
