from homework2.hw1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)

file_name = "./homework2/data.txt"


def test_func_1():
    """Testing that function 1 returns
    right answer"""
    result = [
        "einzelwissenschaften",
        "entscheidungsschlacht",
        "geschichtsphilosophie",
        "gewissenserforschung",
        "menschenfreundlichen",
        "millionenbevölkerung",
        "selbstbezichtigungen",
        "verfassungsverletzungen",
        "werkstättenlandschaft",
        "wiederbelebungsübungen",
    ]
    assert get_longest_diverse_words(file_name) == result


def test_func_2():
    """Testing that function 2 returns
    right answer"""
    result = "î"
    assert get_rarest_char(file_name) == result


def test_func_3():
    """Testing that function 3 returns
    right answer"""
    result = 5475
    assert count_punctuation_chars(file_name) == result


def test_func_4():
    """Testing that function 4 returns
    right answer"""
    result = 2972
    assert count_non_ascii_chars(file_name) == result


def test_func_5():
    """Testing that function 4 returns
    right answer"""
    result = "ä"
    assert get_most_common_non_ascii_char(file_name) == result
