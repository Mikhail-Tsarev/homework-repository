from pathlib import Path

from homework9.hw3 import universal_file_counter


def test__case_without_tokenizer(tmpdir):
    """Testing case without tokenizer"""

    tmpdir.join(f"text1.txt").write("0\n1\n2\n3\n4\n5\n6\n")
    tmpdir.join(f"text2.txt").write("7\n8\n9\n")
    tmpdir.join(f"text3.txt").write("10\n11\n12\n")
    assert universal_file_counter(Path(str(tmpdir)), "txt") == 13


def test_case_with_split_tokenizer(tmpdir):
    """Testing case with tokenizer"""

    tmpdir.join(f"text1.txt").write("0 1\n2\n3\n")
    tmpdir.join(f"text2.txt").write("4\n5\n6 7 8 9\n")
    assert (universal_file_counter(Path(str(tmpdir)), "txt", str.split)) == 10
