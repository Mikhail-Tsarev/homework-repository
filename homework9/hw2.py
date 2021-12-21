from contextlib import contextmanager


class Suppressor:
    """Context manager to suppress specified exceptions"""

    def __init__(self, exception) -> None:
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exctype, value, traceback):
        if exctype == self.exception:
            return True
        return False


@contextmanager
def suppressor(exception):
    """
    Suppresses specified exceptions

    :param exception: Exceptions
    """

    try:
        yield
    except exception:
        pass
