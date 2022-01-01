from homework7.hw1 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
    "RED": 1,
}


def test_element_is_a_string_case():
    """Testing a case when element is a string"""

    assert find_occurrences(example_tree, "RED") == 7
    assert find_occurrences(example_tree, "of") == 2


def test_element_is_a_list_case():
    """Testing a case when element is a list"""

    assert (
        find_occurrences(
            example_tree, ["simple", "list", "of", "RED", "valued"]
        )
        == 1
    )
