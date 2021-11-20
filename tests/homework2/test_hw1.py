import homework2.hw1 as hw1

file_name = "./homework2/data.txt"
# file_name = "D:\YandexDisk\Python\homework-repository\homework2\data.txt"


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
    assert hw1.get_longest_diverse_words(file_name) == result


def test_func_2():
    """Testing that function 2 returns
    right answer"""
    result = "î"
    assert hw1.get_rarest_char(file_name) == result


def test_func_3():
    """Testing that function 3 returns
    right answer"""
    result = 5475
    assert hw1.count_punctuation_chars(file_name) == result


def test_func_4():
    """Testing that function 4 returns
    right answer"""
    result = 2971
    assert hw1.count_non_ascii_chars(file_name) == result


def test_func_5():
    """Testing that function 4 returns
    right answer"""
    result = "ä"
    assert hw1.get_most_common_non_ascii_char(file_name) == result
