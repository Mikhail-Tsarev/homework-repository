from homework11.hw1 import ColorsEnum, SizesEnum


def test_colorsEnum():
    """Testing that ColorsEnam instance get
    __keys attrs from its metaclass"""

    a = ColorsEnum()
    assert a.BLUE == "BLUE"
    assert a.BLACK == "BLACK"
    assert a.RED == "RED"


def test_sizesEnum():
    """Testing that SizesEnam instance get
    __keys attrs from its metaclass"""

    b = SizesEnum()
    assert b.XL == "XL"
    assert b.L == "L"
    assert b.S == "S"
