from homework7.hw2 import is_same_input


def test_positive_case():
    """Test equal strings without hashtags"""
    assert is_same_input("abc", "abc") is True


def test_one_hashtag_case():
    """Test equal lowercase strings with hashtag"""
    assert is_same_input("ab#c", "acc#") is True


def test_several_hashtags_case():
    """Test equal lowercase strings with several hashtags"""
    assert is_same_input("a#a#c", "a##c") is True


def test_negative_case():
    """Test non equal stings"""
    assert is_same_input("a#c", "a#c#") is False
