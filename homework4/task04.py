from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Return list of n FizzBuzz numbers, n is an exact integer
    >>> fizzbuzz(5)
    [1, 2, 'fizz', 4, 'buzz']
    >>> fizzbuzz(15) # doctest: +NORMALIZE_WHITESPACE
    [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz',\
    'buzz', 11, 'fizz', 13, 14, 'fizzbuzz']
    >>> fizzbuzz(0)
    []
    >>> fizzbuzz(-1)
    []
    >>> fizzbuzz(1.2)
    Traceback (most recent call last):
        ...
    ValueError: n must be an integer
    """

    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    return [
        "fizzbuzz"
        if number % 15 == 0
        else "buzz"
        if number % 5 == 0
        else "fizz"
        if number % 3 == 0
        else number
        for number in range(1, n + 1)
    ]


if __name__ == "__main__":

    import doctest

    doctest.testmod()
