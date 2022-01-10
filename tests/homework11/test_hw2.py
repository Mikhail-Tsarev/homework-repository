from homework11.hw2 import Order


def morning_discount(order):
    return order * 0.5


def elder_discount(order):
    return order * 0.9


def test_order_with_discount_case():
    """Testing that class takes different discount programs"""

    assert Order(100, morning_discount).final_price() == 50
    assert Order(100, elder_discount).final_price() == 10


def test_no_discount_case():
    """Testing that class work without discount program"""

    assert Order(100).final_price() == 100
