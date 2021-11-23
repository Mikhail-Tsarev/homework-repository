import pytest

from homework3.task03 import make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


@pytest.mark.parametrize(
    ["kwargs", "sample_data", "expected"],
    [
        ({"kind": "parrot", "type": "bird"}, sample_data, sample_data[1]),
        ({"last_name": "Gilbert"}, sample_data, sample_data[0]),
    ],
)
def test_make_filter(kwargs, sample_data, expected):
    """Assert make_filter returns expected"""

    assert make_filter(**kwargs).apply(sample_data) == [expected]
