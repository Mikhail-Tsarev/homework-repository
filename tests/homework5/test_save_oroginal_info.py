import functools

from homework5.save_original_info import print_result


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


def test_print_result_doc():
    """Testing for __doc__ info"""
    assert (
        custom_sum.__doc__
        == """This function can sum any objects which have __add___"""
    )


def test_print_result_name():
    """Testing for __name__ info"""
    assert custom_sum.__name__ == "custom_sum"
