from unittest.mock import patch

import pytest

from homework4.task02 import count_dots_on_i


class FakeResponse:
    status_code = 200
    content = "b'<body>i never forget about i</body>"

    def read(self):
        return self.content.encode()

    def close(self):
        pass


def test_count_dots_on_i():
    """Testing i counter using fake response"""
    fake_response = FakeResponse()

    with patch("homework4.task02.urlopen") as mock_urlopen:
        mock_urlopen.return_value = fake_response
        assert count_dots_on_i("https://google.com/") == 2


def test_wrong_url_case():
    """Testing raise of ValueError"""

    with pytest.raises(ValueError):
        count_dots_on_i("https://this-site-doesnot-exist-i.com/")
