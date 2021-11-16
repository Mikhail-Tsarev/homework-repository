"""
Given a file containing text.
Complete using only default collections:
    1) Find 10 longest words consisting from largest
    amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

import re
import sys
from typing import List
from unicodedata import category


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    Returns 10 longest words consisting from largest
    amount of unique symbols

    :param file_path: File to process
    :return: Sorted list of longest words
    """

    words = set()
    with open(file_path, encoding="unicode_escape") as fi:
        for line in fi:
            words.update(re.findall(r"\w+", line.lower()))
    long_ten = sorted(
        words, key=lambda w: (len(w), len(set(w))), reverse=True
    )[:10]
    return sorted(long_ten)


def get_rarest_char(file_path: str) -> str:
    """
    Returns rarest non punctuation symbol for document

    :param file_path: File to process
    :return: Rarest symbol
    """

    # get unicode punctuation set
    punc_u = (chr(i) for i in range(sys.maxunicode + 1))
    punctuation = set(c for c in punc_u if category(c).startswith("P"))

    counter = dict()
    chars = []
    with open(file_path, encoding="unicode_escape") as fi:
        for line in fi:
            chars.extend([x for x in line.lower() if x not in punctuation])
    for char in chars:
        counter[char] = counter.get(char, 0) + 1
    sorted_counter = sorted(counter, key=counter.get)
    return sorted_counter[0]


def count_punctuation_chars(file_path: str) -> int:
    """
    Returns number of all punctuation
    chars in document

    :param file_path: File to process
    :return: Number of punctuation chars
    """

    # get unicode punctuation set
    punc_u = (chr(i) for i in range(sys.maxunicode + 1))
    punctuation = set(c for c in punc_u if category(c).startswith("P"))

    counter = 0
    with open(file_path, encoding="unicode_escape") as fi:
        for line in fi:
            for char in line:
                if char in punctuation:
                    counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    """
    Returns number of all
    non-ascii chars in document

    :param file_path: File to process
    :return: Number of non-ascii chars
    """

    # get all ascii chars string
    ascii_chars = "".join(chr(c) for c in range(128))

    counter = 0
    with open(file_path, encoding="unicode_escape") as fi:
        for line in fi:
            for char in line:
                if char not in ascii_chars:
                    counter += 1
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    Returns most common non-punctuation
    non-ascii char in document

    :param file_path: File to process
    :return: Most common symbol
    """

    # get all ascii chars string
    ascii_chars = "".join(chr(c) for c in range(128))

    # get unicode punctuation
    punc_u = (chr(i) for i in range(sys.maxunicode + 1))
    punctuation = set(c for c in punc_u if category(c).startswith("P"))

    counter = dict()
    chars = []
    with open(file_path, encoding="unicode_escape") as fi:
        for line in fi:
            chars.extend(
                [
                    c
                    for c in line.lower()
                    if (c not in ascii_chars and c not in punctuation)
                ]
            )
    for char in chars:
        counter[char] = counter.get(char, 0) + 1
    sorted_counter = sorted(counter, key=counter.get, reverse=True)
    return sorted_counter[0]
