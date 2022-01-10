"""
Given two strings. Return if they are equal
when both are typed into empty text editors.
# means a backspace character.
Note that after backspacing an empty text,
the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""

from itertools import zip_longest


def gen_chars(line: str) -> str:
    """
    Generates chars from the end of a string,
    interpreting '#' as a backspace command
    (skipping previous !='#' symbol)

    :param line: Input string
    """

    cnt = 0
    for char in line[::-1]:
        if char == "#":
            cnt += 1
            continue
        if cnt > 0:
            cnt -= 1
            continue
        yield char


def is_same_input(first: str, second: str) -> bool:
    """
    Compares given strings equality if we interpret
    '#'  as a backspace command deleting symbol
    in front of it

    :param first: First string to compare
    :param second: Second string to compare
    :return: Are strings the same
    """

    for f, s in zip_longest(gen_chars(first), gen_chars(second)):
        if f != s:
            return False
    return True
