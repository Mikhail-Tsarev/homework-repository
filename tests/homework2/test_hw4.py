from homework2.hw4 import cache


def test_math_func_case():
    """Testing with math func"""

    def f(a, b):
        return (a ** b) ** 2

    cache_func = cache(f)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2
