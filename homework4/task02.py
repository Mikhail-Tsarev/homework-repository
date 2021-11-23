from urllib.request import urlopen


def count_dots_on_i(url: str) -> int:
    """
    Function to count 'i' symbol on the of web-page

    :param url: Web-page to process
    :return: Amount of 'i' on the page
    """

    with urlopen(url) as response:
        html = response.read().decode("utf-8")
        return html.count("i")
