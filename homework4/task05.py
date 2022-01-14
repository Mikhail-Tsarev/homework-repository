from itertools import cycle
from typing import Generator


def fizzbuzz(n: int) -> Generator:
    """Return generator of n FizzBuzz numbers, n is an exact integer

    :param n: Integer, last number in generator
    :return: Generator of FizzBuzz sequence from 1 to n

    >>> list(fizzbuzz(5))
    ['1', '2', 'fizz', '4', 'buzz']
    >>> list(fizzbuzz(15)) # doctest: +NORMALIZE_WHITESPACE
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz',\
    'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    >>> list(fizzbuzz(0))
    []
    >>> list(fizzbuzz(-1))
    []
    >>> list(fizzbuzz(1.2))
    Traceback (most recent call last):
        ...
    ValueError: n must be an integer
    """

    def fizzbuzz_gen():
        """Yields right sequence of fizz, buzz and numbers
        from 1 to n"""

        fizz = cycle(("", "", "fizz"))
        buzz = cycle(("", "", "", "", "buzz"))
        nums = [str(i) for i in range(1, n + 1)]

        for i in range(0, n):
            yield next(fizz) + next(buzz) or str(nums[i])

    if isinstance(n, int):
        return fizzbuzz_gen()
    raise ValueError("n must be an integer")


if __name__ == "__main__":

    import doctest

    doctest.testmod()
