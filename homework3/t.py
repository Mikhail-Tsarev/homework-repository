from functools import wraps


def make_fun(func):
    @wraps(func)
    def wrapper():
        ans = func() * 2
        return f"FUN!!! {ans} FUN!!!"

    return wrapper()


@make_fun
def h():
    """

    :rtype: object
    """
    return "got it "


print(h.__doc__)
