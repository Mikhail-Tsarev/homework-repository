from homework8.task02 import TableData

file_name = "/homework8/example.sqlite"

storage = TableData(file_name, "presidents")


def test_len_method_case():
    """Checking for records number in presidents table"""

    assert len(storage) == 3


def test_get_record_from_table_case():
    """Checking for 'Yeltsin' in table"""

    record = storage["Yeltsin"]
    record_data = [record[key] for key in record.keys()]
    assert record_data == ["Yeltsin", 999, "Russia"]


def test_data_in_table_case():
    """Checking for positive in example"""

    assert "Yeltsin" in storage


def test_data_not_in_table_case():
    """Checking for 'Musk' not in table"""

    assert "Musk" not in storage


def test_iter_method_case():
    """Checking if storage object can be iterated through"""

    names_list = [line["name"] for line in storage]
    assert names_list == ["Yeltsin", "Trump", "Big Man Tyrone"]
