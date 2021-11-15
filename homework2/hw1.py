"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import re
from typing import List

file_name = "data.txt"


def get_longest_diverse_words(file_path: str) -> List[str]:
    words = set()
    with open(file_name, encoding="unicode_escape") as fi:
        for line in fi:
            words.update(re.findall(r"\w+", line.lower()))

    return sorted(words, key=lambda w: len(set(w)), reverse=True)[:10]


def get_rarest_char(file_path: str) -> str:
    pass


def count_punctuation_chars(file_path: str) -> int:
    pass


def count_non_ascii_chars(file_path: str) -> int:
    pass


def get_most_common_non_ascii_char(file_path: str) -> str:
    pass


print(get_longest_diverse_words(file_name))
