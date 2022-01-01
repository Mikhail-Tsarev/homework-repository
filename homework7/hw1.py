from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    """
    Takes an element and finds the number of its occurrences
    in given dict containing multiple nested structures

    :param tree: Dict for search in it
    :param element: Element to count its occurrences
    :return: Number of elements occurrences
    """

    def finder(branch: dict, element: Any):
        """
        Auxiliary function to go through nested
        structures and count elements/
        Result is stored in nonlocal 'cnt' variable

        :param branch: Structure to search trough
        :param element: Element to count its occurrences
        """
        nonlocal cnt

        if branch == element:
            cnt += 1

        if isinstance(branch, dict):
            for value in branch.values():
                finder(value, element)

        if isinstance(branch, (list, tuple, set)):
            for el in branch:
                finder(el, element)

    cnt = 0

    for el in tree:
        if el == element:
            cnt += 1

    finder(tree, element)

    return cnt
