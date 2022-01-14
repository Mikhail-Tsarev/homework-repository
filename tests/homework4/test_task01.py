import os

import pytest

from homework4.task01 import read_magic_number


@pytest.fixture()
def file_gen(file_path, val):
    with open(file_path, "w") as fi:
        fi.write(val)


@pytest.mark.parametrize(
    ["file_path", "val"],
    [
        ("data0.txt", "1"),
        ("data1.txt", "2.5\n"),
        ("data2.txt", "1.99\n33\n78"),
    ],
)
def test_read_magic_number_positive_case(file_path, val, file_gen):
    """Testing that we get True with test files"""

    result = read_magic_number(file_path)
    os.remove(file_path)
    assert result is True


@pytest.mark.parametrize(
    ["file_path", "val"],
    [("data3.txt", "-15"), ("data4.txt", "0"), ("data5.txt", "3\n56\n24\n")],
)
def test_read_magic_number_negative_case(file_path, val, file_gen):
    """Testing that we get False with test files"""

    result = read_magic_number(file_path)
    os.remove(file_path)
    assert result is False


@pytest.mark.parametrize(
    ["file_path", "val"],
    [
        ("data6.txt", "sad"),
        ("data7.txt", ""),
        ("data8.txt", "2err"),
    ],
)
def test_read_magic_number_value_error_case(file_path, val, file_gen):
    """Testing that we get ValueError Exception with test files"""

    with pytest.raises(ValueError):
        read_magic_number(file_path)
    os.remove(file_path)
