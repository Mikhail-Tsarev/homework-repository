from homework9.hw1 import merge_sorted_files

# file1 = "./homework9/file1.txt"
# file2 = "./homework9/file1.txt"
file1 = "D:\YandexDisk\Python\homework-repository\homework9\\file1.txt"
file2 = "D:\YandexDisk\Python\homework-repository\homework9\\file2.txt"

l = [file1, file2]


def test_return_type():
    """Testing that we get iterator"""

    assert hasattr(merge_sorted_files(l), "__iter__")


def test_with_2_files():
    """Testing that we get correct answer"""

    assert list(merge_sorted_files(l)) == [1, 2, 3, 4, 5, 6]
