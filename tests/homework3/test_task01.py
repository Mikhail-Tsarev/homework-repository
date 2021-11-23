from homework3.task01 import cashe_times


def test_sum_of_float_powers_case_times2():
    """Testing that decorated sum_of_powers func
    returns cashe 2 times only"""

    @cashe_times(2)
    def sum_of_float_powers(a: float, b: float) -> float:
        return a ** b + b ** a

    a, b, c, d = (sum_of_float_powers(2.2, 3.3) for _ in range(4))
    assert a is b and b is c and c is not d


def test_sum_of_float_powers_case_times0():
    """Testing that decorated sum_of_powers func
    returns cashe everytime"""

    @cashe_times()
    def sum_of_float_powers(a: float, b: float) -> float:
        return a ** b + b ** a

    a, b, c, d = (sum_of_float_powers(2.2, 3.3) for _ in range(4))
    assert a is b and b is c and c is d
