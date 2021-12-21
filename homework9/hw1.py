from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """
    Merges integers from files listed in file_list and returns
    iterator

    :param file_list: List of paths or str file names
    :return: Iterator
    """

    result = []
    for file in file_list:
        with open(file) as fi:
            integers = [int(line.strip()) for line in fi.readlines()]
            result.extend(integers)
    return iter(sorted(result))
