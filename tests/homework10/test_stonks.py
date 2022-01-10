from bs4 import BeautifulSoup

from homework10.stonks import get_main_page_link, get_soup


def test_get_soup():
    """Testing that we get BeautifulSoup object"""

    assert isinstance(get_soup("https://ya.ru/"), BeautifulSoup)


def test_get_main_page():
    """Testing that we get main page of the website from url"""
    assert (
        get_main_page_link("https://training.ru/#!/About?lang=ru", ".ru")
        == "https://training.ru"
    )
